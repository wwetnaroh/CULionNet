<template>
  <div class="container">
    <el-container>
      <el-header class="m-header"><Header /></el-header>
      <el-main style="margin-top: -20px;">
        <el-row style="text-align: center; margin: 20px;">
          <el-col :span="3"></el-col>
          <el-col :span="18" style="box-shadow: 0px 0px 5px #808080;">
            <div class="background">
              <img
                style="width: 100%; height: 300px;"
                src="/assets/columbia.png"
              />
            </div>
            <div class="img">
              <el-row style="margin-top: -60px">
                <el-col :span="6" >  
                  <div class="userimg" style="width: 200px; height: 200px"></div>
                </el-col>
                <el-col :span="18"></el-col>
              </el-row>
            </div>
            <div class="content">
              <div style="border-bottom: solid #a0a0a0">
                <el-row>
                  <el-col :span="6"></el-col>
                  <el-col
                    style="margin-top: 50px; text-align: left; font-size: 15px"
                    :span="13"
                  >
                    <p style="font-size: 15px" >
                      <span style="font-size: 35px">{{ username }}</span> &emsp;
                      <a :href="'https://' + github"
                        v-if="github"><img
                          style=""
                          src="/assets/github.png"
                          width="20"
                        /> </a
                      >&nbsp;
                      <a :href="'https://' + linkedin"
                        v-if="linkedin"><img
                          style=""
                          src="/assets/linkedin.png"
                          width="20"
                        />
                      </a>
                    </p>
                    <p style="margin-top: -10px">
                      {{ state }} <br />
                      Email: {{ email }} &emsp;&emsp;&nbsp; Major: {{ major }}
                    </p>
                  </el-col>
                  <el-col :span="5" style="margin-top: 50px; font-size: 20px">
                    <a
                      href=""
                      style="color: black; font-size: 20px; margin-left: 120px"
                      @click.prevent="edit"
                      ><el-icon><Edit /></el-icon>
                    </a>
                    <el-dialog
                      class="customWidth"
                      v-model="dialogFormVisible"
                      title="Edit profile"
                      width="45%"
                    >
                      <el-form :model="form">
                        <el-form-item
                          label="Headline"
                          label-width="'80px'"
                        >
                          <el-input
                            v-model="form.headline"
                            autocomplete="off"
                          />
                        </el-form-item>
                        <el-form-item
                          label="Major"
                          :label-width="'80px'"
                        >
                          <el-input    
                            v-model="form.major"
                            autocomplete="off"
                          />
                        </el-form-item>
                        <el-form-item
                          label="Linkedin"
                          :label-width="'80px'"
                        >
                          <el-input v-model="form.linked" autocomplete="off">
                            <template #prepend>Https://</template>
                          </el-input>
                        </el-form-item>
                        <el-form-item
                          label="Github"
                          :label-width="'80px'"
                        >
                          <el-input v-model="form.github" autocomplete="off">
                            <template #prepend>Https://</template>
                          </el-input>
                        </el-form-item>
                        <div style="text-align: left; width: 90%; margin: 0px auto; margin-bottom: 10px;">
                          Course available: <span v-for="course in alreadyHave" :key="course.id">
                            {{course.code}} &nbsp;                       
                          </span>
                        </div>
                        <el-form-item
                          label="Course enrolled"
                          :label-width="'140px'"
                        >
                          <vue-tags-input
                            v-model="tag"
                            style="width: 70%"
                            :tags="tags"
                            @tags-changed="(newTags) => (tags = newTags)"
                          />
                          
                        </el-form-item>
                      </el-form>
                      <div style="width: 50%;">
                        <input id="upload-input" type="file" accept="image/gif, image/jpg, image/png" @change="preview"/>
                        <div class="preview">
                        </div>
                      </div>
                      <template #footer>
                        <span class="dialog-footer">
                          <el-button @click="dialogFormVisible = false"
                            >Cancel</el-button
                          >
                          <el-button type="primary" @click="finishEdit"
                            >Confirm</el-button
                          >
                        </span>
                      </template>
                    </el-dialog>
                  </el-col>
                </el-row>
              </div>
              <div class="information">
                <el-row>
                  <el-col
                    style="border-right: solid 2px #808080; margin: 10px"
                    :span="14"
                  >
                    <h5>Posted Thread</h5>
                    <div class="singletopic" v-for="thread in threadList" :key="thread.id">
                      <router-link :to="'/' + thread.topic + '/' + thread.id">
                        <div class="name">{{ thread.id.split('|')[0] }}</div>
                      </router-link>
                    </div>
                  </el-col>
                  <el-col style="margin-top: 10px" :span="9">
                    <el-row>
                      <el-col :span="18">
                        <h5>Enrolled Courses</h5>
                        <div class="singlecourse" v-for="course in profileCourseList" :key="course">
                          <router-link :to="'/course/' + course">
                            <div class="courseletter">{{ course }}</div>
                          </router-link>                      
                        </div>
                      </el-col>
                      <el-col  :span="6">
                        <a
                          href=""
                          style="color: black; font-size: 20px;"
                          @click.prevent="deletecourse"
                          ><el-icon style="margin-left: 40px"><Delete /></el-icon>
                        </a>
                        <el-dialog
                          class="customWidth"
                          v-model="deletedialogFormVisible"
                          title="Edit profile"
                          width="45%"
                        >
                          <el-form :model="form">
                            <el-form-item
                              label="Course enrolled"
                              :label-width="formLabelWidth"
                            >
                              <vue-tags-input
                                v-model="tag"
                                :tags="tags"
                                @tags-changed="(newTags) => (tags = newTags)"
                              />
                            </el-form-item>
                          </el-form>
                          <template #footer>
                            <span class="dialog-footer">
                              <el-button @click="deletedialogFormVisible = false"
                                >Cancel</el-button
                              >
                              <el-button type="primary" @click="deleteFinished"
                                >Confirm</el-button
                              >
                            </span>
                          </template>
                        </el-dialog>
                      </el-col>
                    </el-row>
                  </el-col>
                </el-row>
              </div>
            </div>
          </el-col>
          <el-col :span="3"></el-col>
        </el-row>
        <div></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "./Header.vue";
import { Edit } from "@element-plus/icons-vue";
import { Delete } from "@element-plus/icons-vue";
import VueTagsInput from "@sipec/vue3-tags-input";
import axios from "axios";

const formLabelWidth = '300px'

export default {
  name: "profile",
  components: {
    Header,
    Edit,
    Delete,
    VueTagsInput,
  },
  data() {
    return {
      form: {
        major: "",
        linked: "",
        github: "",
        headline: "",
        courseList: [],
        deleteList: [],
      },
      username: this.$cookies.get("username"),
      email: this.$cookies.get("email"),
      major: "",
      state: "",
      github: "",
      linkedin: "",
      dialogFormVisible: false,
      tag: "",
      tags: [],
      threadList: [],
      threadURL: [],
      profileCourseList: [],
      enrolledList: [],
      deletedList: [],
      operation: "",
      deletedialogFormVisible: false,
      imgSrc: "/assets/columbia.png",
      imgFormVisible: false,
      alreadyHave: [],
      alreadyHaveName: [],
      event: {},
      url: "",
    };
  },
  methods: {
    loginResponse: function (res) {
      if (res == "success") {
        this.$cookies.set("username", this.form.username, 60 * 60 * 24 * 7);
        console.log(this.$cookies.get("username"));
        this.$router.push("/");
      }
    },
    onSubmit: function () {},
    edit: function () {
      this.dialogFormVisible = true;
    },
    finishEdit: function () {
      this.dialogFormVisible = false;
      for (let i = 0; i < this.tags.length; i++) {
        this.enrolledList.push(this.tags[i].text);
      }    
      for (let i = 0; i < this.enrolledList.length; i++) {
        if (this.alreadyHaveName.indexOf(this.enrolledList[i]) == -1) {
          this.enrolledList = [];
          this.tags = [];
          alert("The course is not available yet");
        }
      }
      if (!this.enrolledList) {
        this.enrolledList = [];
      }
      this.operation = "edit";
      if (!this.form.linked) {
        this.form.linked = "";
      }
      if (!this.form.github) {
        this.form.github = "";
      }
      if (!this.form.headline) {
        this.form.headline = "";
      }
      if (!this.form.major) {
        this.form.major = "";
      }  

      console.log("event: ", this.event);
      if (JSON.stringify(this.event) !== '{}') {
        // console.log("upload photo")
        var file = this.event.target.files[0];
        // console.log("file: ", file.name)
        var type = file.name.split(".")[1]
        let reader = new FileReader();    
        var name = this.username;                         
        reader.readAsDataURL(file);
        reader.addEventListener('load',function(){
          var imgBase64 = this.result.split(',')[1];
          var header = {
            "Content-Type": "image/" + type + ";base64",
            "Accept": '*/*',
            'filename': name + '_' + 'img',
          };
          console.log("header: ", header)           
          axios
            .put("https://fza3mueei0.execute-api.us-east-1.amazonaws.com/TRY/upload", imgBase64, {
              headers: header
            })
            .then((res) => {
              console.log("upload success");     
            })
            .catch(function (error) {
              console.log(error);
            });
        })
        var url = "https://6998projphoto.s3.amazonaws.com/" + name + '_' + 'img';  
        console.log("url: ", url)  
        axios
        .post(
          "https://w6149o7ew5.execute-api.us-east-1.amazonaws.com/API_9/modify_course",
          { user: this.username, major: this.form.major, headline: this.form.headline,  linkedin: this.form.linked, github: this.form.github, courselist: this.enrolledList, operation: this.operation, img: url, editImg: true }
        )
        .then((res) => {
          console.log("post done")
          console.log(res);
          this.enrolledList = [];
          this.tags = [];
          this.operation = "";
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });  
      } else {
        var edit = false;
        if (typeof(this.url)=='undefined') {
          var url = "/assets/somebody.png";
          edit = true;
        } else {
          edit = false;
        }        
        axios
          .post(
            "https://w6149o7ew5.execute-api.us-east-1.amazonaws.com/API_9/modify_course",
            { user: this.username, major: this.form.major, headline: this.form.headline,  linkedin: this.form.linked, github: this.form.github, courselist: this.enrolledList, operation: this.operation, img: "", editImg: edit }
          )
          .then((res) => {
            console.log(res);
            this.enrolledList = [];
            this.tags = [];
            this.operation = "";
            // this.$router.go(0);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    deletecourse: function() {
      this.deletedialogFormVisible = true;
    },
    deleteFinished: function() {
      if (this.profileCourseList.length == 0) {
        alert("No course added yet");
        return;
      }
      this.deletedialogFormVisible = false;
      for (let i = 0; i < this.tags.length; i++) {
        this.deletedList.push(this.tags[i].text);
      }
      console.log('deletedList: ',this.deletedList)
      console.log('profileCourseList: ',this.profileCourseList)
      for (let i = 0; i < this.deletedList.length; i++) {
        if (this.profileCourseList.indexOf(this.deletedList[i]) == -1) {
          this.deletedList = [];
          this.tags = [];
          alert("You don't have this course")
          return;
        }
      }
      console.log(this.deletedList)
      this.operation = "delete";
      axios
        .post(
          "https://w6149o7ew5.execute-api.us-east-1.amazonaws.com/API_9/modify_course",
          { user: this.username, major: this.form.major, headline: this.form.headline,  linkedin: this.form.linked, github: this.form.github, courselist: this.deletedList, operation: this.operation }
        )
        .then((res) => {
          console.log(res);
          this.deletedList = [];
          this.operation = "";
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });
        // this.$router.go(0);
    },
    uploadImg: function() {
      this.imgFormVisible = true;
    },
    preview: function(event) {
      console.log(event)
      this.event = event;
      var div = document.querySelector('.preview');
      var file = event.target.files[0];
      let reader = new FileReader();                         
      reader.readAsDataURL(file);
      reader.addEventListener('load',function(){
        var img = document.createElement('img');
        img.src = this.result;
        img.height = "150";
        img.width = "150";
        div.appendChild(img);
      })
    }
  },
  mounted() {
    axios
      .get(
        "https://lv2gvn5vqe.execute-api.us-east-1.amazonaws.com/API_10/get_profile",
        { params: { username : this.username } }
      )
      .then((res) => {
        console.log(res.data)
        this.major = res.data.major;
        this.state = res.data.headline;
        this.github = res.data.github;
        this.linkedin = res.data.linkedin;
        this.profileCourseList = res.data.courselist;
        this.threadURL = res.data.thread_list;
        this.form.major = this.major;
        this.form.linked = this.linkedin;
        this.form.github = this.github;
        this.form.headline = this.state;
        this.url = res.data.img;
        console.log("this url: , typeof(url)", this.url, typeof(this.url))
        if (typeof(this.url)=='undefined') {
          this.url = "/assets/somebody.png";
          console.log("no url")
          var userImg = document.querySelector('.userimg');
          var img = document.createElement('img');
          console.log("url: ", this.url)
          img.src = this.url;
          img.style.borderRadius = "50%";
          img.style.border = "solid white";
          img.width = "140";
          img.height = "140";
          img.style.marginLeft = "30px";
          userImg.appendChild(img);
          return
        }

        let urlSet = new Set();
        this.threadURL.forEach(function(item, index, array) {
          urlSet.add(item);
        })
        // console.log("urlSet: ", urlSet)
        // threadList
        for (var url of urlSet) { // 遍历Array
          this.threadList.push(url)
        }
        // console.log(this.threadList)

        var userImg = document.querySelector('.userimg');
        var img = document.createElement('img');
        console.log("url: ", this.url)
        img.src = this.url;
        img.style.borderRadius = "50%";
        img.style.border = "solid white";
        img.width = "140";
        img.height = "140";
        img.style.marginLeft = "30px";
        userImg.appendChild(img);
      });
    axios
      .get(
        "https://bu5abp0lyf.execute-api.us-east-1.amazonaws.com/API_13/get_all_courses",
        { params: {} }
      )
      .then((res) => {
        // console.log(res.data);
        // alreadyHave
        this.alreadyHave = res.data.course_list;
        for (let item of this.alreadyHave) {
          this.alreadyHaveName.push(item['code']);
        }
        console.log(this.alreadyHaveName)
      })
      .catch(function (error) {
        console.log(error);
      });

    
  },
  created() {
    // this.profileCourseList
    
  },
};
</script>

<style scoped>
.m-header {
  height: 110px !important;
  --el-header-padding: 0px;
}

.el-container.is-vertical {
  background-color: #e0e0e0;
}

.container {
  max-width: 100% !important;
  width: 100%;
  height: 100%;
  padding: 0px;
  margin: 0px;
  background-color: #e0e0e0;
}

.background {
  width: 100%;
  height: 300px;
  margin-top: -20px;
}

.content {
  width: 100%;
  background-color: white;
  margin-top: -180px;
}

.customWidth {
  width: 350px !important;
}

.singletopic {
  border: 1px solid #79cdcd;
  border-radius: 10px;
  margin: 10px;
  font-size: 15px;
  text-align: left;
  box-shadow: 0px 0px 5px #c7c6c6;
}

.name {
  margin: 10px;
  margin-left: 30px;
}

.singlecourse {
  border: 1px solid #79cdcd;
  box-shadow: 0px 0px 5px #c7c6c6;
  width: 100%;
  margin: 10px;
  border-radius: 10px;
  text-align: left;
}

.courseletter {
  margin: 10px;
  margin-left: 20px;
  border-radius: 10px;
  width: 33%;
}

a {
  text-decoration: none;
  color: black;
}

.router-link-active {
  text-decoration: none;
}

</style>
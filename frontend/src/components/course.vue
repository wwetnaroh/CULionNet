<template>
  <div class="container">
    <Header />
    <el-container>
      
      <el-main>
        <div class="courseDesc">
          <el-row gutter="10">
            <el-col :span="16">
              <h1 style="margin: 30px; color: #743AFD; margin-bottom: 10px;">{{courseCode}}</h1>
              <div style="margin-left: 35px; color: #743AFD; font-size: 15px; margin-bottom: 20px;">
                {{courseCode  + ' ' +fullName}}
              </div>
              <el-row :gutter="30">
                <el-col :span="8">
                  <div style="margin-left: 35px; color: black; font-size: 15px; margin-bottom: 5px;"> Department
                    : &nbsp; &nbsp;{{department}}
                  </div>
                </el-col>
              </el-row>
            </el-col>
            <el-col :span="8">
              <div style="margin: 30px; color: black; margin-bottom: 10px; font-size: 25px;">Related Links</div>
              <div style="width: 60%; background-color:white; color:black; box-shadow: 0px 0px 5px #808080; margin-left: 30px; ">      
                <router-link :to="classWeb" style="color: black" v-if="this.classWeb">
                  <p style="margin:10px">Course Website</p>
                </router-link>
              </div>
              <div style="width: 60%; background-color:white; color:black; box-shadow: 0px 0px 5px #808080; margin-left: 30px; margin-top: 15px;">      
                <router-link :to="classWeb" style="color: black">
                  <p style="margin:10px">Department Website</p>
                </router-link>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="stat">
          <div style="font-size: 30px; margin: 10px 0px 10px 30px">
            Details
          </div>
          <el-row :gutter="20">
            <el-col :span="6">
              <div style="margin:10px; margin-bottom: 20px; margin-right: 5px; margin-top: 10px;box-shadow: 0px 0px 5px #808080; width: 90%; text-align: center; height: 195px; background-color: white;border-radius: 10px;">
                <div style="font-size: 20px;">Assessment Type</div>
                <div v-for="assess in assessment" :key="assess.id" style="text-align: left; width: 40%; margin: 0px auto">
                  <div v-if="assess.have" style="margin: 10px 0px 10px 0px; color: #00CC00;">
                    {{assess.name}}<el-icon><Check /></el-icon> 
                  </div>
                  <div v-else style="margin: 10px 0px 10px 0px; color: #C0C0C0;">
                    {{assess.name}}<el-icon><Close /></el-icon> 
                  </div>
                </div>
              </div>  
            </el-col>
            <el-col :span="6">
              <div style="margin:10px; box-shadow: 0px 0px 5px #808080; width: 90%; text-align: center; height: 195px;background-color: white;border-radius: 10px;">
                <div style="font-size: 20px;">Mean GPA: {{meanGPA}} / 4</div>
                <div style="margin: 0px auto; width: 50%;">
                  <circle-progress :percent="gpaperCent" size=160 />
                </div>
              </div>
            </el-col>
            <el-col :span="6">
              <div style="margin:10px; margin-bottom: 20px; box-shadow: 0px 0px 5px #808080; width: 90%; text-align: center; height: 195px;background-color: white;border-radius: 10px;">
                <div style="font-size: 20px;">Nearest Semester</div>
                <div v-for="ss in semester" :key="ss" style="text-align: left; width: 40%; margin: 0px auto">
                  <div style="margin: 10px 0px 10px 0px; color: black;">
                    {{ss}}
                  </div>
                </div>
              </div>
            </el-col>
            <el-col :span="6">
              <div style="margin:10px; box-shadow: 0px 0px 5px #808080; width: 90%; text-align: center; height: 195px;background-color: white;border-radius: 10px;">
                <div style="font-size: 20px;">Workload: {{workload}} / 5</div>
                <div style="margin: 0px auto; width: 50%;">
                  <circle-progress :percent="workloadperCent" size=160 /> 
                </div>            
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="comment">
          <div style="font-size: 30px; margin: 10px 0px 10px 30px">
            Comments ({{commentNum}}) <el-button style="box-shadow: 0px 0px 5px #808080; margin-left: 30px;" type="plain" @click="before" size="large">Add a comment</el-button>
            <el-dialog v-model="courseFormVisible" title="Course details" width="40%" center="false"  >
              <el-form :model="courseForm">
                <span >GPA &nbsp;</span>
                <el-input v-model="form.gpa" autocomplete="off" style="width:13%; margin-bottom: 10px; "/> / 4.0  &nbsp; &nbsp; &nbsp;
                <span >Workload &nbsp; </span>
                <el-input v-model="form.workload" autocomplete="off" style="width:13%; margin-bottom: 10px; "/> / 5.0 &nbsp; &nbsp; &nbsp; 
                <span >Grade &nbsp;(A+ ~ D)&nbsp;&nbsp;</span>
                <el-input v-model="form.grade" autocomplete="off" style="width:13%; margin-bottom: 10px; "/> &nbsp; &nbsp; <br/>
                <span>Instructor &nbsp;</span>
                <el-input v-model="form.instructor" autocomplete="off" style="width:20%; margin-bottom: 10px; "/>&nbsp; &nbsp; 
                <span>Year &nbsp;</span>
                <el-input v-model="form.year" autocomplete="off" style="width:20%; margin-bottom: 10px; "/>&nbsp; &nbsp;
                <span >semester &nbsp;</span>
                <el-select v-model="term" style="width: 23%;">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select> <br/>
                <div style="margin-top: 5px;">Comment</div>
                <br/>
                <el-input style="width: 100%; margin-top: 5px;" v-model="form.comment" autocomplete="off" :rows="4" type="textarea"/>
              </el-form>
              <template #footer>
                <span class="dialog-footer">
                  <el-button @click="courseFormVisible = false">Cancel</el-button>
                  <el-button type="primary" @click="completeCourse"
                    >Confirm</el-button
                  >
                </span>
              </template>
            </el-dialog>
          </div>
          <div v-for="comment in commentUsers" :key="comment.id" style="width: 99%; box-shadow: 0px 0px 5px #808080; background-color: white; margin: 20px 0px 0px 10px; height: 300px; border-radius: 10px;">
            <div class="info">
              <el-row :gutter="20">
                <el-col :span="4">
                  <img
                    style="
                      border-radius: 50%;
                      border: solid white;
                      margin-left: 20px;
                      margin-top: 10px;
                    "
                    :src="comment.new_comment_user_Img"
                    width="90"
                    height="90"
                  />
                </el-col>
                <el-col :span="18"><br/>
                  {{comment.user}} <br/>
                  {{comment.time}}
                </el-col>
                <el-col :span="2">
                  <div style="background-color: #743AFD; width: 90%; color: white; text-align: center; font-size: 30px; margin:20px 40px 0 0;">
                    {{comment.grade}}
                  </div>
                </el-col>
              </el-row>
              <el-row style="margin-left: 20px;margin-top: 10px;margin-bottom: 10px; width: 95%; border-bottom: solid 2px #C0C0C0">
                <el-col :span="5">
                  Semester <br />
                  <b>{{comment.semester}}</b>
                </el-col>
                <el-col :span="5">
                  Instructor <br />
                  <b>{{comment.instructor}}</b>
                </el-col>
                <el-col :span="3">
                  GPA <br/>
                  <b>{{comment.gpa}}</b>
                </el-col>
                <el-col :span="3">
                  Workload <br/>
                  <b>{{comment.workload}}</b>
                </el-col>
                <el-col :span="6">
                </el-col>
              </el-row>
              <div style="margin-left: 20px; margin-top: 10px; width: 90%;">
                {{comment.comments}}
              </div>
            </div>
            <div class="">

            </div>
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "./Header.vue";
import { Link, Check, Close } from "@element-plus/icons-vue";
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import bar from './bar.vue'
import { Bar } from 'vue3-charts'
import axios from "axios";

export default {
  name: "Course",
  components: {
    Header,
    Link,
    CircleProgress,
    Check,
    Close,
    bar,
    Bar,
  },
  data() {
    return {
      user: this.$cookies.get("username"),
      courseCode: this.$route.params.name,
      courseFormVisible: false,
      fullName: "",
      department: "",
      classWeb: "",
      instructor: "",
      departWeb: "",
      meanGPA: "",
      gpaperCent: "",
      workload: "",
      workloadperCent: "",
      semester: [],
      assessment: [
        {
          name: "Assignment",
          have: false
        },
        {
          name: "Project",
          have: false
        },{
          name: "Report",
          have: false
        },
        {
          name: "Exam",
          have: false
        },
      ],
      commentNum: 0,
      form: {
        grade: "",
        gpa: "",
        workload: "",
        semester: "",
        instructor: "",
        comment: "",
        user: "",
        time: "",
        code: "",
        year: "",
      },
      commentUsers: [],
      options: [
        {
          value: 'Fall',
          label: 'Fall',
        },
        {
          value: 'Spring',
          label: 'Spring',
        },
      ],
      term: "Select"
    };
  },
  methods: {
    before: function() {
      this.courseFormVisible = true;
    },
    completeCourse: function() {
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      console.log(this.term)
      this.courseFormVisible = false;
      var myDate = new Date();
      var time = myDate.getFullYear()+"-"+(myDate.getMonth()+1)+"-"+myDate.getDate() + ' ' + myDate.getHours()+"-"+(myDate.getMinutes())+"-"+myDate.getSeconds();
      this.form.user = this.user;
      this.form.time = time;
      this.form.code = this.courseCode;
      this.form.semester = this.form.year + " " + this.term;
      console.log(this.form.semester)
      axios
        .post(
          "https://x5w387ik14.execute-api.us-east-1.amazonaws.com/API_6/post_evaluation",
          { form: this.form }
        )
        .then((res) => {
          console.log(res);
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getCourse: function() {
      axios
        .get(
          "https://kbnrem44zi.execute-api.us-east-1.amazonaws.com/API_5/get_evaluation",
          { params: { course: this.courseCode } }
        )
        .then((res) => {
          console.log(res.data);
          this.fullName = res.data.course;
          this.department = res.data.department;
          this.classWeb = res.data.courseWebsite;
          this.departWeb = res.data.deptWebsite;
          this.assessment[0].have = res.data.assignment;
          this.assessment[1].have = res.data.project;
          this.assessment[2].have = res.data.report;
          this.assessment[3].have = res.data.exam;
          this.semester = res.data.semester;
          this.commentUsers = res.data.comments;
          var gpaList = res.data.GPA;
          var sum = 0;
          for (let i=0;i<gpaList.length;i++){
            gpaList[i] = Number(gpaList[i]);
            sum += gpaList[i];
          }
          this.meanGPA = sum / gpaList.length;
          this.meanGPA = this.meanGPA.toFixed(1);
          console.log("this meanGPA: ", this.meanGPA)
          var workloadList = res.data.workload;
          sum = 0;
          for (let i=0;i<workloadList.length;i++){
            workloadList[i] = Number(workloadList[i]);
            sum += workloadList[i];
          }
          this.workload = sum / workloadList.length;
          this.workload = this.workload.toFixed(1);
          this.gpaperCent = this.meanGPA / 4.0 * 100;
          this.workloadperCent = this.workload / 5.0 * 100;
          if (!this.commentUsers) {
            this.commentNum = 0;
          } else {
            this.commentNum = this.commentUsers.length;
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getCourse();
  },
  created() {
    
  }
}

</script>

<style scoped>
.container {
  max-width: 100% !important;
  width: 100%;
  padding: 0px;
  margin: 0px;
}

.m-header {
  height: 110px !important;
  /* --el-header-padding: 0px !important; */
}

.el-container {
  background-color: #e0e0e0;
}

.el-main {
  --el-main-padding: 0px !important;
}

a {
  text-decoration: none;
}

.router-link-active {
  text-decoration: none;
}

.courseDesc {
  width: 80%;
  margin: 0px auto;
  background-color: #EBE2FF;
}

.stat {
  width: 80%;
  margin: 0px auto;
}

.comment {
  width: 80%;
  margin: 0px auto;
}

</style>

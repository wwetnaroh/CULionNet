<template>
  <div class="container">
    <el-container>
      <el-header class="m-header"><Header /></el-header>
      <el-main>
        <div style="width: 75%; margin: 0px auto; margin-top:20px;">
          <h1>Thread Topic</h1>
        </div>
        <div class="main" style="border-radius: 10px;">
          <el-row style="">
            <el-col :span="6" style="">
              <div class="user">
                <img style="margin-top: 20px;" :src="postUserImg" width="140" height="140">
                <h4 style="margin: 20px;">{{postUser}}</h4><br/>
              </div>
            </el-col>
            <el-col :span="18">
              <div class="content">
              <!-- <div class="subject"> -->
                <span style="margin: 20px 20px 0px 5px; font-size: 30px;">{{subject}}</span>
                
              <!-- </div> -->
              
                <div style="width: 100%; border-bottom: 3px dotted #808080; margin: 0px 0px 0px 0px;">
                  <el-row>
                    <el-col :span="12">
                      <div style="float:left;margin: 10px 0px 0px 10px;">posted by: {{postUser}}</div>
                    </el-col>
                    <el-col :span="12">
                      <span style="float:right;margin: 10px 0px 0px 10px;">posted in: {{postTime}}</span>
                    </el-col>
                  </el-row>   
                </div>
                <div  style="margin: 10px 10px 0px 0px; font-size: 20px;">
                  {{content}}
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
        <el-row style="width: 75%; margin: 0px auto; margin-bottom: 20px;">
          <el-col :span="18">
            <div style="width: 100%; margin: 0px auto; margin-top:20px;">
              <h3>Comments</h3>
            </div>
          </el-col>
          <el-col :span="6">
            <div style="margin:5px; text-align: right; margin-top: 20px; width:90%">
              <el-button type="primary" @click="before" round size="large">Add a comment</el-button>
              <div style="text-align: left">
                <el-dialog v-model="dialogFormVisible" style="text-align: left" title="Post a comment" width="40%">
                  <el-form :model="form">
                    <el-form-item label="Content" :label-width="'70px'">
                      <el-input v-model="form.content" autocomplete="off" :rows="6" type="textarea"/>
                    </el-form-item>
                  </el-form>
                  <template #footer>
                    <span class="dialog-footer">
                      <el-button @click="dialogFormVisible = false">Cancel</el-button>
                      <el-button type="primary" @click="onSubmit"
                        >Confirm</el-button
                      >
                    </span>
                  </template>
                </el-dialog>
              </div>
            </div>
          </el-col>
        </el-row>     
        <div class="comment" v-for="comment in comments" :key="comment.id">
          <el-row style="background-color: white; box-shadow: 0px 0px 5px #808080; margin: 0px auto; margin-bottom: 20px;border-radius: 10px;">
            <el-col :span="6">
              <div class="user">
                <img style="margin-top: 20px;" :src="comment.img" width="140" height="140"> 
                <!-- TODO: change img -->
                <h4 style="margin: 20px;">{{comment.username[0]}}</h4><br/>
              </div>
            </el-col>
            <el-col :span="18">
              <div class="commentccc">
                <div style="width: 93%; border-bottom: 3px dotted #808080; margin: 20px; margin-top:10px;">
                  posted by: {{comment.username[0]}}
                  <span style="float:right;">posted in: {{comment.time[0]}}</span>
                </div>
                <span  style="margin: 20px; margin-top: 40px; font-size: 15px;">
                  {{comment.comment}}
                </span>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="addcomment">

        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "./Header.vue";
import axios from "axios";

export default {
  name: "thread",
  components: {
    Header,
  },
  data() {
    return {
      username: this.$cookies.get("username"),
      id: this.$route.params.id,
      subject: "",
      topic_name: this.$route.params.topicname,
      postUser: "",
      postTime: "",
      content: "",
      comments: [],
      dialogFormVisible: false,
      postUserImg: "",
      form: {
        content: '',
      },
    };
  },
  methods: {
    onSubmit: function () {
      var db = "";
      if (this.topic_name == "Job Hunting") {
        db = "Job_hunting";
      } else if (this.topic_name == "House leasing") {
        db = "House_leasing";
      } else if (this.topic_name == "New York life") {
        db = "NYC_life";
      }
      var myDate = new Date();
      var time = myDate.getFullYear()+"-"+(myDate.getMonth()+1)+"-"+myDate.getDate() + '-' + myDate.getTime();
      var createTime = myDate.getFullYear()+"-"+(myDate.getMonth()+1)+"-"+myDate.getDate()+":"+myDate.getHours()+":"+(myDate.getMinutes())+":"+myDate.getSeconds();
      axios
        .post(
          "https://7dp3niiyuf.execute-api.us-east-1.amazonaws.com/API_3/write_comment",
          { db: db, id: this.id, replier: this.username, time: createTime, new_content: this.form.content, topic: this.topic_name }
        )
        .then((res) => {
          console.log(res);
          this.dialogFormVisible = false;
          this.$router.go(0);
        })
        this.dialogFormVisible = false;
        // this.$router.go(0);
        
    },
    before: function() {
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      this.dialogFormVisible = true;
    }
  },
  created() {
    console.log(this.topic_name)
    console.log(this.subject)
    var db = "";
    if (this.topic_name == "Job Hunting") {
      db = "Job_hunting";
    } else if (this.topic_name == "House leasing") {
      db = "House_leasing";
    } else if (this.topic_name == "New York life") {
      db = "NYC_life";
    }
    axios
      .get(
        "https://7dfiyfjui9.execute-api.us-east-1.amazonaws.com/API_4_thread/get_thread_content",
        { params: { db: db, id: this.id } }
      )
      .then((res) => {
        console.log(res.data);
        this.postUser = res.data.postUser;
        this.postTime = res.data.postTime;
        this.content = res.data.content;
        this.comments = res.data.comments;
        this.subject = res.data.title;
        this.postUserImg = res.data.postUserImg;
        console.log(this.comments)
      });
    
  }
};
</script>

<style scoped>
.el-main {
  --el-main-padding: 0px !important;
}

.m-header {
  height: 110px !important;
  --el-header-padding: 0px;
}

.el-container.is-vertical {
  background-color: #e0e0e0;
}

.container {
  max-width: 100% !important;
  max-height: 100% !important;
  width: 100%;
  height: 100%;
  padding: 0px;
  margin: 0px;
  background-color: #e0e0e0;
}

.main {
  background-color: white;
  width: 75%;
  margin: 0px auto;
  margin-bottom: 10px;
  margin-top: 20px;
  box-shadow: 0px 0px 5px #808080;
}

.user {
  margin-top: 20px;
  margin-left: 30px;
  text-align: center;
  width: 80%;
  height: 85%;
  border-right: solid 2px #C0C0C0
}

.subject {
  background-color: white;
  text-align: left;
  margin-top: 20px;
  /* margin-left: -50px; */
  width: 95%;
}

.content {
  background-color: white;
  text-align: left;
  margin-top: 10px;
  /* margin-left: -50px; */
  width: 95%;
  height: 300px;
  animation: myfirst 1s linear alternate;
}

.commentccc {
  background-color: white;
  text-align: left;
  margin-top: 10px;
  /* margin-left: -50px; */
  width: 95%;
  height: 150px;
}

.comment {
  background-color: #e0e0e0;
  width: 75%;
  margin: 0px auto;
  margin-bottom: 0px;
  animation: myfirst 1s linear alternate;
}

@keyframes myfirst {
  0%   {background-color:rgba(255,255,255,0.2); left:0px; top:20px;}
  25%  {background-color:rgba(255,255,255,0.4);left:0px; top:15px;}
  50%  {background-color:rgba(255,255,255,0.6);left:0px; top:10px;}
  75%  {background-color:rgba(255,255,255,0.8);left:0px; top:5px;}
  100% {background-color:rgba(255,255,255);left:0px; top:0px;}
}

</style>
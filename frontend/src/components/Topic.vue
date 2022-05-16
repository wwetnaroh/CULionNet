<template>
  <div class="container">
    <Header />
    <el-row :gutter="10" class="bar">
      <el-col :span="7" style="text-align: center">
        <h4 class="display-5" style="font-size: 33px">{{ topic_name }}</h4>
      </el-col>
      <el-col :span="12"></el-col>
      <el-col :span="5">
        <el-button type="primary" @click="before" round size="large">Post a Thread</el-button>
        <el-dialog v-model="dialogFormVisible" title="Post a thread" width="40%">
          <el-form :model="form">
            <el-form-item label="Subject" :label-width="'70px'">
              <el-input v-model="form.title" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Content" :label-width="'70px'">
              <br/>
              <el-input v-model="form.content" autocomplete="off" :rows="4" type="textarea"/>
            </el-form-item>
          </el-form>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="dialogFormVisible = false">Cancel</el-button>
              <el-button type="primary" @click="createFinish"
                >Confirm</el-button
              >
            </span>
          </template>
        </el-dialog>
      </el-col>
    </el-row>
    <el-row :gutter="10" class="bar1">
      <el-col :span="1"></el-col>
      <el-col :span="22" class="topic">
        <div class="singletopic" v-for="thread in threadNameList" :key="thread.id">
          <router-link :to="'/' + topic_name + '/' + thread.id" class="topicbutton">
            <div class="name">{{ thread.thread_name }}</div>
          </router-link>
        </div>
      </el-col>
      <el-col :span="1"></el-col>
    </el-row>
  </div>
</template>

<script>
import Header from "./Header.vue";
import axios from "axios";

export default {
  name: "Topic",
  components: {
    Header,
  },
  data() {
    return {
      topic_name: this.$route.params.name,
      username: this.$cookies.get("username"),
      threadNameList: [],
      threadID: [],
      dialogFormVisible: false,
      form: {
        title: '',
        content: '',
      },
    };
  },
  methods: {
    getThread: function () {
      var url = "job-hunting";
      var db;
      if (this.topic_name == "Job Hunting") {
        db = "Job_hunting";
      } else if (this.topic_name == "House leasing") {
        db = "House_leasing";
      } else if (this.topic_name == "New York life") {
        db = "NYC_life";
      } else if (this.topic_name == "Crime Map") {
        url = "crime-map";
      }
      console.log(url);
      axios
        .get(
          "https://sxrclphv22.execute-api.us-east-1.amazonaws.com/API_1_1/" +
            url,
          { params: { topic_name: db } }
        )
        .then((res) => {
          console.log(res.data);
          this.threadNameList = res.data.dict;
        });
    },
    before: function() {
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      this.dialogFormVisible = true;
    },
    createFinish: function() {
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
      var createTime = myDate.getFullYear()+"-"+(myDate.getMonth()+1)+"-"+myDate.getDate();
      var id = this.form.title + '|' + time;
      axios
        .post(
          "https://lqfldh7112.execute-api.us-east-1.amazonaws.com/API_2/write_thread",
          { database: db, user: this.username, t: createTime, title: this.form.title,  main: this.form.content, id: id, topic: this.topic_name }
        )
        .then((res) => {
          console.log(res);
          this.dialogFormVisible = false;
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
          this.dialogFormVisible = false;
          this.$router.go(0);
        });
      
      this.dialogFormVisible = false;
    },
  },
  created() {
    this.getThread();
  },
};
</script>

<style scoped>
.container {
  max-width: 100% !important;
  width: 100%;
  padding: 0px;
  margin: 0px;
}

.bar {
  width: 90%;
  padding: 0px;
  margin-left: 55px !important;
  margin-right: 20px !important;
  margin-top: 35px !important;
  margin-bottom: 20px !important;
  text-align: center;
}

.bar1 {
  width: 90%;
  padding: 0px;
  margin-left: 60px !important;
  margin-right: 20px !important;
}

.topic {
  /* border:1px solid #000; */
  width: 90%;
}

.singletopic {
  border: 1px solid #79cdcd;
  border-radius: 10px;
  margin: 20px;
  font-size: 20px;
  animation: myfirst 1.5s linear alternate;
}

.name {
  margin: 10px;
}

a {
  text-decoration: none;
}

.router-link-active {
  text-decoration: none;
}

@keyframes myfirst {
  0%   {background-color:rgba(255,255,255,0.2); left:0px; top:20px;}
  25%  {background-color:rgba(255,255,255,0.4);left:0px; top:15px;}
  50%  {background-color:rgba(255,255,255,0.6);left:0px; top:10px;}
  75%  {background-color:rgba(255,255,255,0.8);left:0px; top:5px;}
  100% {background-color:rgba(255,255,255);left:0px; top:0px;}
}


</style>

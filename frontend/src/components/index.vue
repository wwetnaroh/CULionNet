<template>
  <div class="container">
    <Header />
    <el-container>
      <el-main>
        <el-row :gutter="10">
          <el-col class="left" :span="2">
            <div style="text-align: center">
              <h5>Check my courses</h5>
              <el-switch v-model="value" v-if="user" @click="change"/>
              <el-switch v-model="value" disabled v-else/>
              <el-button style="margin-top: 30px;" type="primary" @click="courseBefore" size="small">Add a course</el-button>
              <el-dialog v-model="courseFormVisible" title="Course details" width="43%" center="false"  >
                <el-form :model="courseForm">
                  <span >Course Code &nbsp;</span>
                    <el-input v-model="courseForm.code" autocomplete="off" style="width:15%; margin-bottom: 20px; margin-right: 20px;"/>
                  <span >Department &nbsp;</span>
                    <el-input v-model="courseForm.department" autocomplete="off"  style="width:49%; margin-bottom: 20px;"/><br/>
                  <span >Course Name &nbsp;</span>
                    <el-input v-model="courseForm.courseName" autocomplete="off"  style="width:81%; margin-bottom: 20px;"/>&nbsp;&nbsp;
                    <br/>
                  <span >Course Website &nbsp;</span>
                  <el-input v-model="courseForm.courseWebsite" autocomplete="off"  style="width:79%; margin-bottom: 20px;" :rows="2"/><br/>
                  <span >Department Website &nbsp;</span>
                  <el-input v-model="courseForm.deptWebsite" autocomplete="off"  style="width:74%; margin-bottom: 20px;" :rows="2"/><br/>
                  <el-checkbox v-model="courseForm.exam" label="Exam" style="margin-left: 60px; margin-right: 30px;"/>
                  <el-checkbox v-model="courseForm.assignment" label="Assignment" style="margin-left: 20px; margin-right: 30px;"/>
                  <el-checkbox v-model="courseForm.report" label="Report" style="margin-left: 20px; margin-right: 30px;"/>
                  <el-checkbox v-model="courseForm.project" label="Project" style="margin-left: 20px;"/><br /><br />
                  <span >GPA &nbsp;</span>
                  <el-input v-model="courseForm.GPA" autocomplete="off" style="width:6%; margin-bottom: 20px; "/> / 4.0  &nbsp; &nbsp;
                  <span >Workload &nbsp;</span>
                  <el-input v-model="courseForm.workload" autocomplete="off" style="width:6%; margin-bottom: 20px; "/> / 5.0 &nbsp; &nbsp;
                  <span>Year &nbsp;</span>
                  <el-input v-model="courseForm.year" autocomplete="off" style="width:15%; margin-bottom: 20px; "/>&nbsp; &nbsp; 
                  <span >semester &nbsp;</span>
                  <el-select v-model="term" style="width: 15%">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
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
          </el-col>
          <el-col class="course" :span="16">
            <el-row class="coursehere" >
            </el-row>
          </el-col>
          <el-col class="calendar" :span="6">
            <Calendar
              backgroundText
              class-name="select-mode"
              @onSelect="onSelect"
              style="width: 240px; height: 250px; margin: 0px auto"
            />
            <el-row>
              <el-col :span="16">
                <span style="font-size: 25px; margin-top: 15px;margin-left: 20px;">Meeting</span>
              </el-col>
              <el-col :span="8">
                <el-row style="margin-top: 5px;margin-right: 10px;">
                  <el-col :span="12">
                    <el-button type="primary" @click="before" circle >
                      <el-icon><Plus /></el-icon> 
                    </el-button>
                    <el-dialog v-model="dialogFormVisible" title="Meeting details" width="40%">
                      <el-form :model="form">
                        <el-form-item label="Time" :label-width="'90px'">
                          <el-input v-model="form.time" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="Description" :label-width="'90px'">
                          <el-input v-model="form.description" autocomplete="off" />
                        </el-form-item>
                        <el-form-item label="Place" :label-width="'90px'">
                          <el-input v-model="form.place" autocomplete="off" />
                        </el-form-item>
                      </el-form>
                      <template #footer>
                        <span class="dialog-footer">
                          <el-button @click="dialogFormVisible = false">Cancel</el-button>
                          <el-button type="primary" @click="createMeeting"
                            >Confirm
                          </el-button>
                        </span>
                      </template>
                    </el-dialog>
                  </el-col>
                  <el-col :span="12">
                    <el-button type="danger" circle >
                      <el-icon><Delete /></el-icon> 
                    </el-button>
                  </el-col>
                </el-row>
              </el-col>
            </el-row>
            <div class="meet" v-for="meet in meetingList" :key="meet">
              <div class="name">{{ meet }}</div> 
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "./Header.vue";
import Calendar from "mpvue-calendar";
import { Plus } from "@element-plus/icons";
import { Delete } from "@element-plus/icons-vue";
import axios from "axios";

export default {
  name: "Main",
  components: {
    Header,
    Calendar,
    Plus,
    Delete,
  },
  data() {
    return {
      // meetingList: [],
      user: this.$cookies.get("username"),
      meetingList: [],
      form: {
        time: '',
        description: '',
        place: '',
      },
      courseForm: {
        courseName: '',
        code: '',
        department: '',
        courseWebsite: '',
        deptWebsite: '',
        exam: false,
        assignment: false,
        report: false,
        project: false,
        GPA: "",
        workload: "",
        semester: '',
        year: '',
        comment: []
      },
      dialogFormVisible: false,
      courseFormVisible: false,
      date: "",
      value: false,
      course: [
        // {
        //   code: "COMS4113",
        //   name: "distributed system"
        // },
      ],
      color: ['#FF6666', '#FF0000', '#606060', '#009999', '#994C00', '#CC99FF', '#009900', '#999900'],
      userCourse: [
        // {
        //   code: "COMS6998",
        //   name: "cloud computing"
        // },
        // {
        //   code: "ELEN6889",
        //   name: "large scale stream processing"
        // },
      ],
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
      term: "select",
    };
  },
  methods: {
    onSelect: function (selectDate) {
      var date = new Date();
      console.log(date);
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      console.log(selectDate);
      this.date = selectDate;
      axios
        .get(
          "https://2tt95p6wp2.execute-api.us-east-1.amazonaws.com/API_7/get_calender_meeting",
          { params: { user: this.user, date: selectDate } }
        )
        .then((res) => {
          console.log(res.data);
          this.meetingList = res.data.plan;
        });
    },
    createMeeting: function() {
      this.dialogFormVisible = false;
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      axios
        .post(
          "https://3cm25eps60.execute-api.us-east-1.amazonaws.com/API_8/post_meeting",
          { user: this.user, date: this.date, time: this.form.time,  description: this.form.description }
        )
        .then((res) => {
          console.log(res);
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    before: function() {
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      if (this.date == "") {
        alert("Choose date first");
        return;
      }
      this.dialogFormVisible = true;
    },
    courseBefore: function() {
      if (!this.$cookies.get("username")) {
        alert("Please sign in first!");
        console.log("not signed in")
        return;
      }
      this.courseFormVisible = true;
    },
    completeCourse: function() {
      console.log(this.term)
      if (!this.courseForm.courseName) {
        alert("Please enter a course name.");
        return;
      }
      if (!this.courseForm.code) {
        alert("Please enter a course code.");
        return;
      }
      if (!this.courseForm.department) {
        alert("Please enter a department name.");
        return;
      }
      if (!this.courseForm.deptWebsite) {
        alert("Please enter a department website.");
        return;
      }

      this.courseForm.semester = this.courseForm.year + ' ' + this.term;
      this.courseForm.GPA = [this.courseForm.GPA];
      this.courseForm.workload = [this.courseForm.workload];
      this.courseForm.semester = [this.courseForm.semester];

      console.log(this.courseForm)
      axios
        .post(
          "https://9un90z5lji.execute-api.us-east-1.amazonaws.com/API_12/post_course_info",
          { courseForm: this.courseForm }
        )
        .then((res) => {
          console.log(res);
          this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    change: function() {
      var course = document.querySelector('.coursehere');
      var courseList = [];
      if (!this.value) {
        courseList = this.course;
      } else {
        courseList = this.userCourse;
      }
      console.log(courseList)
      while(course.firstChild) { 
	      course.removeChild(course.firstChild); 
	    }
      // console.log("success");
      for (let name of courseList) {
        var colorIdx = Math.floor(Math.random() * 8);
        var colorChose = this.color[colorIdx];
        var div = document.createElement('div');
        div.style.paddingLeft = '2.5px';
        div.style.width = '31%';
        div.style.height = '300px';
        div.style.margin = '10px';
        div.style.paddingRight = '2.5px';
        div.style.display = 'block';
        div.style.minHeight = '1px';
        div.style.maxWidth = '33.3%';
        div.style.float = 'left';
        div.style.boxSizing = 'border-box';
        var a = document.createElement('a');
        a.setAttribute('href', '/course/' + name.code);
        a.style.textDecoration = 'none';
        var fatherDiv = document.createElement('div');
        fatherDiv.style.boxShadow = '0px 0px 5px #808080';
        fatherDiv.style.marginTop = '0px';
        var bar = document.createElement('div');
        bar.style.height = '50px';
        bar.style.backgroundColor = colorChose;
        var coursenamen = document.createElement('div');
        coursenamen.style.height = '65px';
        coursenamen.style.color = colorChose;
        var nameCourse = document.createElement('div');
        nameCourse.style.margin = '15px';
        nameCourse.style.fontSize = '15px';
        nameCourse.innerHTML = name.code + ' ' + name.name;
        coursenamen.appendChild(nameCourse);
        fatherDiv.append(bar);
        fatherDiv.appendChild(coursenamen);
        a.appendChild(fatherDiv);
        div.appendChild(a);
        course.appendChild(div);
        console.log("why")
      }
    }
  },
  mounted: function() {
    axios
      .get(
        "https://bu5abp0lyf.execute-api.us-east-1.amazonaws.com/API_13/get_all_courses",
        { params: {} }
      )
      .then((res) => {
        // console.log(res.data);
        this.course = res.data.course_list;
        // console.log(this.course)
        var course = document.querySelector('.coursehere');
        var courseList = [];
        courseList = this.course;

        // console.log(courseList)
        for (let name of courseList) {
          var colorIdx = Math.floor(Math.random() * 8);
          var colorChose = this.color[colorIdx];
          var div = document.createElement('div');
          div.style.paddingLeft = '2.5px';
          div.style.width = '31%';
          div.style.margin = '10px';
          div.style.paddingRight = '2.5px';
          div.style.display = 'block';
          div.style.minHeight = '1px';
          div.style.maxWidth = '33.3%';
          div.style.float = 'left';
          div.style.boxSizing = 'border-box';
          var a = document.createElement('a');
          a.setAttribute('href', '/course/' + name.code);
          a.style.textDecoration = 'none';
          var fatherDiv = document.createElement('div');
          fatherDiv.style.boxShadow = '0px 0px 5px #808080';
          fatherDiv.style.marginTop = '0px';
          var bar = document.createElement('div');
          bar.style.height = '50px';
          bar.style.backgroundColor = colorChose;
          var coursenamen = document.createElement('div');
          coursenamen.style.height = '65px';
          coursenamen.style.color = colorChose;
          var nameCourse = document.createElement('div');
          nameCourse.style.margin = '15px';
          nameCourse.style.fontSize = '15px';
          nameCourse.innerHTML = name.code + ' ' + name.name;
          coursenamen.appendChild(nameCourse);
          fatherDiv.append(bar);
          fatherDiv.appendChild(coursenamen);
          a.appendChild(fatherDiv);
          div.appendChild(a);
          course.appendChild(div);
        }
      })
      .catch(function (error) {
        console.log(error);
      });
      axios
      .get(
        "https://lv2gvn5vqe.execute-api.us-east-1.amazonaws.com/API_10/get_profile",
        { params: { username : this.user } }
      )
      .then((res) => {
        // console.log(res.data)
        var courseList = this.course;
        var user = res.data.courselist;
        console.log(res.data.courselist)
        console.log(courseList)
        for (let code of user) {
          console.log('code:', code)
          for (var item of courseList) {
            if (code == item.code) {
              this.userCourse.push(item);
            }
          }
        }
        console.log(this.userCourse)
      });
  },
  created() {
    
  }
};
</script>

<style scoped>
.container {
  max-width: 100% !important;
  width: 100%;
  padding: 0px;
  margin: 0px;
}

.test a{
	text-decoration: none;
}

.router-link-active {
  text-decoration: none;
}

.course {
  border-right: 2px solid #C0C0C0;
  border-left: 2px solid #C0C0C0;
}

.meet {
  border: 1px solid #79cdcd;
  border-radius: 10px;
  margin: 20px;
  font-size: 20px;
}

.name {
  margin: 5px;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.bar {
  height: 50px;
  background-color: #FF6666;
}

.coursenamen {
  height: 65px;
  color: #FF6666;
}

.coursehere {
  position: relative;
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

<template>
  <div class="container">
    <el-container>
      <el-header class="m-header"><Header /></el-header>
      <el-main>
        <el-row style="text-align: center; margin: 15px">
          <el-col :span="7"></el-col>
          <el-col :span="10">
            <h1>CU LION</h1>
          </el-col>
          <el-col :span="7"></el-col>
        </el-row>
        <el-row style="text-align: center; margin-top: 10px">
          <el-col :span="7"></el-col>
          <el-col :span="10">
            <div class="loginbox">
              <el-row style="text-align: left; margin-top: 10px">
                <el-col :span="2"></el-col>
                <el-col :span="20">
                  <h5 style="margin-bottom: 40px; margin-top: 30px">
                    Register Account
                  </h5>
                  <span style="font-size: 15px">Username</span>
                  <el-input
                    v-model="form.username"
                    placeholder="Please input username"
                    style="margin-top: 5px; margin-bottom: 20px"
                    clearable
                  />
                  <span style="font-size: 15px">Email</span>
                  <el-input
                    v-model="form.email"
                    placeholder="Please input Email"
                    style="margin-top: 5px; margin-bottom: 20px"
                    clearable
                  />
                  <span style="font-size: 15px">Password</span>
                  <el-input
                    v-model="form.password"
                    type="password"
                    placeholder="Please input password"
                    style="margin-top: 5px; margin-bottom: 20px"
                    clearable
                  />
                  <span style="font-size: 15px">Confirmed password</span>
                  <el-input
                    v-model="form.confirmedPassword"
                    type="password"
                    placeholder="Please input password again"
                    style="margin-top: 5px; margin-bottom: 20px"
                    clearable
                  />
                  <span style="font-size: 15px">Verfication Code</span>
                  <el-row style="margin-bottom: 45px">
                    <el-col :span="17">
                      <el-input
                        v-model="form.verify"
                        placeholder="Please input verification code"
                        style="margin-top: 5px"
                        clearable
                      />
                    </el-col>
                    <el-col :span="1"> </el-col>
                    <el-col :span="6" style="margin-top: 5px">
                      <el-button @click="sendCode" :disabled="isSend">{{
                        buttonText
                      }}</el-button>
                    </el-col>
                  </el-row>
                  <el-row style="margin-bottom: 30px">
                    <el-col :span="16">
                      <span style="font-size: 15px">Have an account?</span>
                      <router-link
                        to="/login"
                        style="font-size: 15px; margin-left: 5px"
                        >Sign in</router-link
                      >
                    </el-col>
                    <el-col :span="8">
                      <el-button type="primary" @click="onSubmit" size="large"
                        >REGISTER</el-button
                      >
                    </el-col>
                  </el-row>
                </el-col>
                <el-col :span="2"></el-col>
              </el-row>
            </div>
          </el-col>
          <el-col :span="7"></el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Header from "./Header.vue";
import { RegisterUser, ConfirmEmail } from "../app/auth.js";
import axios from "axios";

export default {
  name: "register",
  components: {
    Header,
  },
  data() {
    return {
      form: {
        email: "",
        password: "",
        confirmedPassword: "",
        username: "",
        verify: "",
      },
      isSend: false,
      count: 30,
      buttonText: "Send code",
    };
  },
  methods: {
    onSubmit: function () {
      if (!this.form.username) {
        alert("Please enter a username.");
        return;
      }
      var reg = /^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/;
      if (!reg.test(this.form.email)) {
        alert("Please enter a valid email address.");
        return;
      }
      if (!this.form.password) {
        alert("Please enter a password.");
        return;
      }
      if (
        !this.form.confirmedPassword ||
        this.form.confirmedPassword != this.form.password
      ) {
        alert("Please enter the password again.");
        return;
      }
      ConfirmEmail(this.form.username, this.form.verify, this.registerResponse);
      axios
        .post(
          "https://w6149o7ew5.execute-api.us-east-1.amazonaws.com/API_9/modify_course",
          { user: this.form.username, major: "", headline: "",  linkedin: "", github: "", courselist: [], operation: "" }
        )
        .then((res) => {
          console.log(res);
          // this.$router.go(0);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    registerResponse: function (response) {
      console.log(response);
      if (response == "success") {
        alert("Register successfully!");
        this.$router.push("/");
      }
    },
    sendCode: function () {
      if (!this.form.username) {
        alert("Please enter a username.");
        return;
      }
      var reg = /^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/;
      if (!reg.test(this.form.email)) {
        alert("Please enter a valid email address.");
        return;
      }
      if (!this.form.password) {
        alert("Please enter a password.");
        return;
      }
      if (
        !this.form.confirmedPassword ||
        this.form.confirmedPassword != this.form.password
      ) {
        alert("Please enter the password again.");
        return;
      }
      var countDown = setInterval(() => {
        if (this.count < 1) {
          this.isSend = false;
          this.buttonText = "Send Code";
        } else {
          this.isSend = true;
          this.count--;
          this.buttonText = this.count + "s Resend";
        }
      }, 1000);
      this.count = 30;

      RegisterUser(
        this.form.username,
        this.form.password,
        this.form.email,
        function (user) {
          console.log(user);
        }
      );
    },
  },
};
</script>

<style scoped>
.el-main {
  --el-main-padding: 0px !important;
}

.el-container.is-vertical {
  background-color: #e0e0e0;
}

.m-header {
  height: 110px !important;
  --el-header-padding: 0px;
}

.loginbox {
  border-radius: 4px;
  border: 1px solid #808080;
  box-shadow: 0px 0px 5px #808080;
  background-color: white;
}

.container {
  max-width: 100% !important;
  width: 100%;
  height: 100%;
  padding: 0px;
  margin: 0px;
  background-color: #e0e0e0;
}
</style>
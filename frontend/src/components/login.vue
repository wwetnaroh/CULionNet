<template>
  <div class="container">
    <el-container>
      <el-header class="m-header"><Header /></el-header>
      <el-main>
        <el-row style="text-align: center; margin: 20px">
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
                    Sign In Account
                  </h5>
                  <span style="font-size: 15px">Username</span>
                  <el-input
                    v-model="form.username"
                    placeholder="Please input email"
                    style="margin-top: 5px; margin-bottom: 20px"
                    clearable
                  />
                  <span style="font-size: 15px">Password</span>
                  <el-input
                    v-model="form.password"
                    type="password"
                    placeholder="Please input password"
                    style="margin-top: 5px; margin-bottom: 45px"
                    clearable
                  />
                  <el-row style="text-align: left">
                    <el-col :span="16">
                      <span style="font-size: 15px">No account?</span>
                      <router-link
                        to="/register"
                        style="font-size: 15px; margin-left: 5px"
                        >Create account</router-link
                      >
                    </el-col>
                    <el-col :span="8">
                      <el-button
                        type="primary"
                        @click="onSubmit"
                        size="large"
                        style="margin-bottom: 40px"
                        >SIGN IN</el-button
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
import { Loginfunc } from "../app/auth.js";

export default {
  name: "login",
  components: {
    Header,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    loginResponse: function (res) {
      if (res["res"] == "success") {
        this.$cookies.set("username", this.form.username, 60 * 60 * 24 * 7);
        this.$cookies.set("email", res["email"], 60 * 60 * 24 * 7);
        console.log(this.$cookies.get("username"));
        this.$router.push("/");
      }
    },
    onSubmit: function () {
      // var reg = /^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/;
      // if (!reg.test(this.form.email)) {
      //     alert("Please enter a valid email address.");
      //     return;
      // }
      if (!this.form.username) {
        alert("Please enter a username.");
        return;
      }
      if (!this.form.password) {
        alert("Please enter a password.");
        return;
      }
      Loginfunc(this.form.username, this.form.password, this.loginResponse);
    },
  },
};
</script>

<style scoped>
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
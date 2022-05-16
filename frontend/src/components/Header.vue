<template>
  <div id="Headerr">
    <div style="width: 15%; height: 110px; float: left">
      <router-link to="/"
        ><img style="height: 90px" src="/assets/Lions.png"
      /></router-link>
    </div>
    <div style="width: 50%; height: 110px; float: left">
      <el-row :gutter="10">
        <el-col class="elrow" :span="6" v-for="name in topicName" :key="name">
          <router-link :to="'/topic/' + name" class="topicbutton" v-if="name != 'Crime Map'">{{
            name
          }}</router-link>
          <a href="https://maps.nyc.gov/crime/" class="topicbutton" v-else>{{
            name
          }}</a>
        </el-col>
      </el-row>
    </div>
    <div style="width: 25%; height: 110px; float: right">
      <el-row :gutter="10" v-if="cookieUser">
        <el-col :span="2"></el-col>
        <el-col class="elrow" :span="10">
          <router-link :to="'/profile/' + cookieUser" style="color: white; font-size: 16px"
            >User Profile</router-link
          >
        </el-col>
        <el-col class="elrow" :span="8">
          <a
            href=""
            style="color: white; font-size: 16px"
            @click.prevent="signOut"
            >Sign Out
          </a>
        </el-col>
        <el-col :span="4"></el-col>
      </el-row>
      <el-row :gutter="10" v-else>
        <el-col :span="4"></el-col>
        <el-col class="elrow" :span="8">
          <router-link to="/login" style="color: white; font-size: 16px"
            >Sign in</router-link
          >
        </el-col>
        <el-col class="elrow" :span="8">
          <router-link to="/register" style="color: white; font-size: 16px"
            >Register</router-link
          >
        </el-col>
        <el-col :span="4"></el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router'

export default {
  name: "Header",
  data() {
    return {
      topicName: ["Job Hunting", "House leasing", "New York life", "Crime Map"],
      cookieUser: this.$cookies.get("username")
        ? this.$cookies.get("username")
        : null,
    };
  },
  methods: {
    signOut: function () {
      if (this.$route.path == '/profile/' + this.cookieUser) {
        this.$cookies.remove("username");
        this.$cookies.remove("email");
        this.$router.push('/');
        return;
      }
      this.$cookies.remove("username");
      this.$cookies.remove("email");
      this.$router.go(0);
      // console.log(this.$route.path)
    },
  },
};
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-col {
  border-radius: 4px;
}

a {
  text-decoration: none;
}

.router-link-active {
  text-decoration: none;
}

.topicbutton {
  color: white;
  font-size: 16px;
}

.elrow {
  height: 110px;
  line-height: 110px;
}

.elrow:hover {
  background-color: #03acac;
  transition: background-color 0.5s;
}

#Headerr {
  width: 100%;
  height: 110px;
  display: block;
  text-align: center;
  padding: 0px;
  margin: 0px;
  background-color: #79cdcd;
}
</style>

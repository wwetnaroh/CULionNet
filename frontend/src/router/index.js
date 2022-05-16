import { createWebHistory, createRouter } from "vue-router"
// import Index from "@/components/index.vue"
import Login from "@/components/login.vue"
import Topic from "@/components/Topic.vue"
import Index from "@/components/index.vue"
import Register from "@/components/register.vue"
import Profile from "@/components/profile.vue"
import Thread from "@/components/thread.vue"
import Course from "@/components/course.vue"

const routes = [
  {
    path: "/",
    name: "Index",
    component: Index,
    meta: {
      title: "proj"
    }
  },
  {
    path: "/topic/:name",
    name: "topic",
    component: Topic,
    meta: {
      title: "proj"
    }
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    meta: {
      title: "proj1-3"
    }
  },
  {
    path: "/register",
    name: "register",
    component: Register,
    meta: {
      title: "proj1-3"
    }
  },
  {
    path: "/profile/:username",
    name: "profile",
    component: Profile,
    meta: {
      title: "proj1-3"
    }
  },
  {
    path: "/:topicname/:id",
    name: "thread",
    component: Thread,
    meta: {
      title: "proj1-3"
    }
  },
  {
    path: "/course/:name",
    name: "course",
    component: Course,
    meta: {
      title: "proj1-3"
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

    
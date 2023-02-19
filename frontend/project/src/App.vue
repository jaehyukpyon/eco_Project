<template>
  <status-bar></status-bar>
  <shinhan-navigation-bar :currentPath="currentPath"></shinhan-navigation-bar>
  <router-view @sendCurrentPath="receiveCurrentPath"></router-view>
  <shinhan-footer-navigation></shinhan-footer-navigation>
</template>

<script>
import StatusBar from "./components/StatusBar.vue";
import ShinhanNavigationBar from "./components/ShinhanNavigationBar.vue";
import ShinhanFooterNavigation from "./components/ShinhanFooterNavigation.vue";

export default {
  data() {
    return {
      currentPath: "",
    };
  },
  components: {
    ShinhanNavigationBar,
    StatusBar,
    ShinhanFooterNavigation,
  },
  methods: {
    receiveCurrentPath(currentPath) {
      console.log('currentPath > ' + currentPath);
      this.currentPath = currentPath;
    }
  },
  mounted() {
  },
};
</script>

<style>
</style>

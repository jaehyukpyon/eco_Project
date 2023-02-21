<template>
  <status-bar></status-bar>  
  <router-view></router-view>
  <shinhan-footer-navigation></shinhan-footer-navigation>
</template>

<script>
import StatusBar from "./components/StatusBar.vue";
import ShinhanNavigationBar from "./components/ShinhanNavigationBar.vue";
import ShinhanFooterNavigation from "./components/ShinhanFooterNavigation.vue";
import GreenBar from "./components/GreenBar.vue";

export default {
  data() {
    return {
      currentPath: "",
      barType: '',
    };
  },
  components: {
    ShinhanNavigationBar,
    StatusBar,
    ShinhanFooterNavigation,
    GreenBar,
  },
  methods: {
    receiveCurrentPath(currentPath) {
      console.log('currentPath > ' + currentPath);
      this.currentPath = currentPath;
    },
    getBarType(barType1) {
      console.log('barType > ' + barType1);
      this.barType = barType1;
    },
  },
  mounted() {
  },
};
</script>

<style>
</style>

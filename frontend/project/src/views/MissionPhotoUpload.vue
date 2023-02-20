<template>
  <div></div>
</template>

<script>
export default {
  data() {},
  methods: {},
  beforeCreate() {
    this.$emit("sendCurrentPath", this.$route.path);
    this.$emit("barType", "shinhan");
  },
};
</script>

<style>
</style>
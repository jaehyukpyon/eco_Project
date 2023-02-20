<template>
  <div>
    <div class="img" style="margin-top:10px; text-aligen: right; position: relative">
      <div v-if="type === 'topname'"></div>
      <img src="../assets/topname/topname.png" width="480" height="160" alt=""/>
    </div>
    <div class="item" style="margin-left:40px; text-align: left;">
      <span>매장명</span>
    </div>
    <div class="item" style="margin-left:100px; text-align: left;">
      <span>지점</span>
    </div>
    <div class="item" style="margin-left:100px; text-align: left;">
      <span>인증만료일</span>
    </div>
    <div class="img" style="margin-top:0px; text-aligen: center; position: relative">
      <div v-if="type === 'bar'"></div>
      <img src="../assets/topname/bar.png" width="480" height="40" alt=""/>
    </div>
  </div>
    <div class="item" style="margin-left:100px; text-align: left;">
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>
      <span class="list">이마트 성수점 23/02/24</span>

    </div>
  <!-- <list-item :listData="list"></list-item> -->
  </template>
  <script>
// import ListItem from '../components/ListItem.vue';
export default {
  // components: { ListItem },
  emits: ["topName", "bar"],
  data() {
    return {
      type: "topname",
      type: "bar",
    };
  },
  methods: {},
  created() {
    // this.$store.dispatch('FETCH_LIST', 'eco_list')
  },
};
</script>
<style scoped>

div.item {
  display: inline-block;
  font-weight : bold;
  font-size: 20px;
}
.eco-name {
  width: 400px;
  height: 200px;
  line-height: 100px;
  margin: 0 auto;
  background-color: white;
  border-radius: 50px;
}
.eco-name > div {
  text-align: center;
}
.eco-name {
  font-size: 70px;
}
.eco-name > span {
  margin: 0 auto;
}
.list {
  display: inline-block;
  font-weight : Normal;
  font-size: 20px;
  position: center;
}
</style>
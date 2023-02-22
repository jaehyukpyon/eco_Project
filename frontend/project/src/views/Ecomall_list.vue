<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="width: 100px; height: 100px; background-color: white; position: absolute; top: 165px; left: 0px; z-index: 100;"></div>
    <div>
      <div
        class="img"
        style="margin-top: 10px; text-aligen: right; position: relative"
      >
        <div v-if="type === 'topname'"></div>
        <img
          src="../assets/topname/topname.png"
          width="480"
          height="160"
          alt=""
        />
      </div>
      <div class="item" style="margin-left: 40px; text-align: left">
        <span>매장명</span>
      </div>
      <div class="item" style="margin-left: 100px; text-align: left">
        <span>지점</span>
      </div>
      <div class="item" style="margin-left: 100px; text-align: left">
        <span>인증만료일</span>
      </div>
      <div
        class="img"
        style="margin-top: 0px; text-aligen: center; position: relative"
      >
        <div v-if="type === 'bar'"></div>
        <img src="../assets/topname/bar.png" width="480" height="40" alt="" />
      </div>
    </div>
    <div style="height: 405px; overflow: auto;">
      <table>
        <tbody style="text-align: center">
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
          <tr>
            <td>이마트</td>
            <td>성수점</td>
            <td>2023/11/23</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'
export default {
  //emits: ["topName", "bar"],
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      type: "topname",
      type: "bar",
      list: [
        {
          name: '이마트',
          loc: '성수점',
          exp: '2023.11.13'
        },
      ]
    };
  },
  methods: {},
  created() {},
};
</script>
<style scoped>
table {
  width: 100%;
}
table tbody {
  width: 100%;
}
table td {
  width: 33.3333%;
}

tr {
  height: 45px;
}
div.item {
  display: inline-block;
  font-weight: bold;
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
  font-weight: Normal;
  font-size: 20px;
  position: center;
}
</style>
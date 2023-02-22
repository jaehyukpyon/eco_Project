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
        <span>업체명</span>
      </div>
      <div class="item" style="margin-left: 100px; text-align: left">
        <span>매장명</span>
      </div>
      <div class="item" style="margin-left: 100px; text-align: left">
        <span>인증만료일</span>
      </div>
      <div
        class="img"
        style="margin-top: 0px; text-aligen: center; position: relative"
      >
        <div v-if="type === 'bar'"></div>
        <img src="../assets/topname/bar.png" width="480" height="40" alt='' />
      </div>
    </div>
    <div style="height: 405px; overflow: auto;">
      <table>
        <tbody style="text-align: center">
          <tr v-for="(item, index) in greenMarket">
            <td>{{ item['업체명']}}</td>
            <td>{{ item['매장명']}}</td>
            <td>{{ item['지정기간'].substr(13, 10) }}</td>
          </tr>          
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'
import axios from 'axios'

export default {
  //emits: ["topName", "bar"],
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      type: "topname",
      type: "bar",
      greenMarket: null,
    };
  },
  methods: {},
  created() {
    const that = this;
    const url = 'https://api.odcloud.kr/api/15043633/v1/uddi:a76efb81-83c1-4f51-9e20-b3e27a5ee186?page=1&perPage=50&serviceKey=pzrN8H960G93rU0CszxDfKi2qHrbWd20Douh32F6cX%2FQU4oB9yUwp3Ew%2FN2KlMSjV%2F%2FgsekEGV5kpcIhYDDJDA%3D%3D';
    axios.get(url)
      .then(response => {
        console.log('녹색매장 리스트');
        console.log(response.data.data)
        that.greenMarket = response.data.data;
        //console.log('greenMarket??')
        //console.log(greenMarket)
      }).catch(error => {
        console.log('녹색기업 크롤링 중 오류발생')
        console.log(error)
      })
  },
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
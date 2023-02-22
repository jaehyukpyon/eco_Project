<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="text-align: center;">
      <img src="../assets/re100/re100.png" alt="">
    </div>
    <div style="height: 328px; overflow: auto; background='red';">
      <table style="text-align: center; width: 100%">
        <thead>
          <tr>
            <th>No.</th>
            <th>기업명</th>
            <th>RE100 달성 <br>목표 연도(년)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in list" :key="item.no">
            <td>{{ item.no }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.when }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';
import axios from 'axios'
export default {
  data() {
    return {
      list: [],
    }
  },
  components: {
    ShinhanNavigationBar,
  },
  created() {
    // backend에서 크롤링한 re100 기업 리스트 받아오기
    const that = this;
    axios.get('http://127.0.0.1:8000/news/inner_text/')
      .then(response => {
        console.log('re100 list response.data')
        console.log(response.data)
        const resultList = response.data;
        resultList.forEach(company => {
          that.list.push({
            no: company[0],
            name: company[2],
            when: company[6].slice(0, 4),
          });
        });
      })
  },
}
</script>

<style scoped>
table thead th {
  height: 45px;
  font-size: 1.3rem;
}

th, td {
  width: 33.333%;
}
tbody td {
  height: 40px;
  font-size: 1.2rem;
}
</style>
<template>
  <div>
    <button @click="addMission(0)">텀블러</button>
    <button @click="addMission(1)">분리수거</button>
    <button @click="addMission(2)">대중교통</button>
    <button @click="addMission(3)">장바구니</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      addmissionList: [
        {
          title: '텀블러사용하기',
          description: '테이크아웃 음료가 텀블러에 담긴 사진을 업로드해주세요.',
          mileage_reward: 10,
        },
        {
          title: '분리수거하기',
          description: '분리수거 한 사진을 업로드해주세요.',
          mileage_reward: 10,
        },
        {
          title: '대중교통이용하기',
          description: '버스/지하철을 이용한 사진을 업로드해주세요.',
          mileage_reward: 10,
        },
        {
          title: '장바구니사용하기',
          description: '다회용 장바구니를 사용한 사진을 업로드해주세요.',
          mileage_reward: 10,
        },
      ]
    };
  },
  methods: {
    created() {
      const url = 'http://34.64.235.73/api/mission/';
      const accessToken = this.$cookies.get('accessToken');
      const that = this;
      for (let i = 0; i < 4; i++) {
        setTimeout(() => {
          axios.post(url, that.addmissionList[i], {
          headers: {
            Authorization: 'JWT ' + accessToken,
          }
          }).then(result => {
            console.log(result.data);
          })
        }, 2000);        
      }


      
    },
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <button @click="addMission">미션 넣기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      missionList: [
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
    addMission() {
      const url = 'http://127.0.0.1:8000/mission/';
      const accessToken = this.$cookies.get('accessToken');

      this.missionList.forEach(mission => {
        axios.post(url, mission, {
          headers: {
            Authorization: 'JWT ' + accessToken,
          }
        }).then(result => {
          console.log('mission 등록 완료!');
          console.log(mission);
        })
      })
    },
  }
}
</script>

<style scoped>

</style>
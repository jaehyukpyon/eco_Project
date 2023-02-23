<template>

  <!-- 
    중요! 데일리 미션 인증을 시현해보기 위해서는
    http://127.0.0.1:8000/addmission 에 접속해서 좌측부터 버튼을 한 번씩 클릭해야 합니다.
    (즉, 맨 좌측의 버튼이 가장 먼저 클릭돼서 pk가 1번이 돼야 함!!!)
   -->
  <div>
    <div>
    <div>
      <p>
        <span class="title" style="margin-top:40px; text-align: center; position: relative; width: 100%;">친환경 인증 데일리 미션</span><br />
        <span class="sub" style="margin-top: 10px; text-align: center; position: relative; width:100%;">일상에서 실천할 수 있는<b></b><br>친환경 활동들을 인증 시<br />
        마일리지로 보상해드립니다!</span>
      </p>
    </div>
  </div>
  <div class="img" style="margin-top: 50px; text-align: center; position: relative;">
      <div v-if="type === 'eco_mission_none'"></div>
      <img src="../assets/eco_mission/mission_none.png" width="400" height="200" alt=""/>
      <img class="change" src="../assets/eco_mission/mission_done.png" width="50" height="50" style="position: absolute; top: 60px; left: 345px;" @click="changeType">
      
      <div v-if="type === 'eco_mission_done'"></div>
      <img src="../assets/eco_mission/mission_done.png" width="400" height="200" alt=""/>
      <img class="change" src="../assets/eco_mission/mission_none.png" width="50" height="50" style="position: absolute; top: 60px; left: 345px;" @click="changeType">
    </div>
  </div>
  
</template>
<script>

export default ({
  data() {
    return {
      type: "eco_mission",
    }
  },
  methods: {
    changeType() {
      if(this.type=='eco_mission_none') this.type='mission_done'
      else if(this.type == 'eco_mission_done') this.type='mission_none'
    }
  },
});
</script>
<style scoped>
.title {
  display: inline-block;
  font-weight: bold;
  font-size: 38px;
  position: center;
  color: #25bf8b;
}
.sub {
  display: inline-block;
  font-weight: normal;
  font-size: 18px;
  position: center;
  color: black;
}
</style>

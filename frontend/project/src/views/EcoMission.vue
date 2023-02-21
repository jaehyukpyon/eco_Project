<template>
  <div>
    <div>
    <div>
      <p>
        <span class="title" style="margin-top:40px; text-align: center; position: relative; width: 100%;">에코 인증 미션</span><br />
        <span class="sub" style="margin-top: 40px; text-align: center; position: relative; width:100%;">일상에서 실천할 수 있는<b></b><br>친환경 활동들을<br />
        인증 시 마일리지 보상!</span>
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
  font-size: 32px;
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

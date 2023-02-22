<template>
  <div>
    <div class="top">
      <p style="margin-left: 25px; font-weight: bolder; font-size: 1.5rem;">친환경 계좌개설</p>
      <br>
      <div class="line" style="width: 100%; height: 0.5px; background-color: lightgray"></div>
    </div>

    <div style="margin-left: 25px; margin-top: 15px;">
      <div>
        <p>더 맑은 내일을 위해</p>
        <p><span style="font-weight: bolder; font-size: 1.2rem">신한투자증권</span>과</p>
        <p>함께하세요.</p>
      </div>
    </div>

    <div class="account">
      <div style="margin-left: 25px">
        <div style="margin-top: 15px;">
          <p>친환경</p>
        </div>
        <div class="line" style="width: 100%; height: 0.5px; background-color: #25BF8B"></div>
        <div style="margin-top: 10px">
          <p>지구를 지키면</p>
          <p><span style="font-weight: bolder; font-size: 1.2rem">마일리지</span>가 쌓이는 만능 계좌</p>
        </div>
        <div>
          <ul style="font-size: 0.9rem; margin-left: 25px; margin-top: 10px">
            <li>&#183; 매일 초기화 되는 데일리 미션 수행 시 마일리지 적립</li>
            <li>&#183; RE100 가입 기업 매수 시 매수금액의 0.2% 마일리지 &nbsp;&nbsp;적립</li>
            <li>&#183; 금융투자상품권 구매가능</li>
            <li>&#183; 녹색매장에서 친환경 상품 구매가능</li>
          </ul>
        </div>
      </div>
      <div @click="move" class="start">
        <div style="position: relative;">
          <p style="color: #25BF8B; font-weight: bolder; font-size: 1.2rem; position: absolute; top: 12px; left: 117px;">계좌개설 시작하기!</p>
        </div>
      </div>
    </div>

    <div style="position: absolute; top: 587px; right: 0px;">
      <img src="../assets/account/characters.png">
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    move() {
      this.$router.push('/account/confirm')
    },
  }
}
</script>

<style scoped>
.start {
  width: 390px;
  height: 55px;  
  position: absolute;
  top: 245px;
  left: 0px;
  background-color: #DEDCDC;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.start:hover {
  cursor: pointer;
}
.account {
  width: 100%;
  height: 0.5px;
  background-color: lightgrey;
  position: absolute;
  top: 250px;
  left: 45px;
  width: 350px;
}

.account {
  background: #fff;
  height: 300px;
  width: 390px;
  border-radius: 20px;
}
.account {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}

.account:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}
</style>
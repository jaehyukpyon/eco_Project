<template>  
    <div>  
        <shinhan-navigation-bar></shinhan-navigation-bar>
        <div>
            <p>
            <span class="title" style="margin-top:65px; text-align: center; position: relative; width: 100%;">친환경 계좌</span><br />
            <span class="sub" style="margin-top: 0px; text-align: center; position: relative; width:100%;">개설이 완료되었습니다!</span>
            </p>
        </div>
        <div style="text-align: center; margin-top: 65px;">
            <img src="../assets/account/account.png" alt="">
        </div>
        
        <div class="finished" @click="finished" style="background: #25BF8B; margin-top: 100px; height: 70px; position: relative;">
            <div>
                <p style="position: absolute; top: 15px; left: 215px; font-size: 1.5rem; color: #fff">확인</p>
            </div>
        </div>
    </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'

export default {
    components: {
        ShinhanNavigationBar
    },
    data() {
        return {
            name: 'done',
        }
    },
    methods: {
        btn_confrim: function(event) {
            alert('친환경 계좌 개설이 완료되셨습니다!')
        }, 
        finished() {
            this.$router.push('/mileage');
        }
    }
}
</script>

<style scoped>
.finished {
    cursor: pointer;
}
.title {
  display: inline-block;
  font-weight: normal;
  font-size: 45px;
  position: center;
  color: #25BF8B;
}
.sub {
  display: inline-block;
  font-weight: light;
  font-size: 35px;
  position: center;
}
.done {
    display: inline-block;
    font: bold;
    font-size: 20px;
    color: white;
    position: center;
}
button {
    background-color: #25BF8B;
    color: white;
    padding: 18px 225.25px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    font-size: 1.2rem;
  }

</style>
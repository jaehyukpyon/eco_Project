<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="top-wrap">
      <img src="../assets/re100/orderstock.png" alt="">
      <img class="buybtn" @click="buyClick" src="../assets/re100/buy2.png" alt="">
    </div>
    <span class="username">변재혁</span>
    <span class="accountnumber">계좌번호: 123456787</span>
    <span class="stockname">삼성바이오로직스</span>
    <span class="stockprice">800000원</span>
    <span class="stockprice-forcalc">800000원</span>
    <span class="quantity">2주</span>
    <span class="ment">지급받을 수 있는 예상 마일리지</span>
    <span class="mileage-calc">1600</span>
    <span class="plus"> + </span>
    <span class="minus"> - </span>

    <div class="modal">
      <div style="text-align:center; font-size: 2.5rem">
        <span>매수 주문확인</span>
      </div>
      <div>
        <table>
          <tbody>
            <tr>
              <td class="title" style="width: 191px!important">종&nbsp;&nbsp;&nbsp;목</td>
              <td class="text">삼성바이오로직스</td>
            </tr>
            <tr>
              <td class="title">주문수량</td>
              <td class="text">10주</td>
            </tr>
            <tr>
              <td class="title">주문가격</td>
              <td class="text">800000주</td>
            </tr>
            <tr>
              <td class="title">거래금액</td>
              <td class="text">800000주</td>
            </tr>
            <tr>
              <td class="title">마일리지</td>
              <td class="text">1600</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      click: false,
      username: null,
      accountnumber: null,
      stockname: null,
      stockprice: null,

    };
  },
  methods: {

  },
}
</script>

<style scoped>
.top-wrap {
  width: 480px;
  height: 645px;
  background-color: white;
  text-align: center;
  position: relative;
}

.buybtn {
  position: absolute;
  top: 590px;
  right: 12px;
}

.buybtn:hover {
  cursor: pointer;
}

.username,
.accountnumber,
.stockname,
.stockprice,
.stockprice-forcalc,
.quantity,
.mileage-calc,
.plus,
.ment,
.minus {
  position: absolute;
}

.username {
  top: 0px;
  left: 0px;
  font-size: 2rem;
  top: 280px;
  left: 34px;
}

.accountnumber {
  top: 0px;
  left: 0px;
  font-size: 1.5rem;
  top: 285px;
  left: 150px;
}

.stockname {
  top: 141px;
  left: 51px;
  font-size: 2.2rem;
}

.stockprice {
  top: 200px;
  left: 25px;
  font-size: 3rem;
}

.stockprice-forcalc {
  top: 620px;
  right: 90px;
  font-size: 1.5rem;
}

.quantity {
  top: 572px;
  right: 123px;
  font-size: 1.5rem;
}

.mileage-calc {
  top: 500px;
  right: 235px;
  font-size: 1.8rem;
}

.ment {
  top: 470px;
  right: 5px;
  font-size: 1.5rem;
}

.modal {
  background: #fff;
  border-radius: 2px;
  display: inline-block;
  height: 350px;
  margin: 1rem;
  position: absolute;
  top: 243px;
  left: 31px;
  width: 400px;
  border-radius: 10px;
}

.modal {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}

.modal:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

.title {
  font-size: 1.8rem;
}
td {
  height: 50px;
}

.text {
  font-size: 1.5rem;
}

table {
  margin-left: 31px;
}
</style>
<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="top-wrap">
      <img src="../assets/re100/orderstock.png" alt="">
      <img class="buybtn" @click="confirmModalToggle" src="../assets/re100/buy2.png" alt="">
    </div>
    <span class="username">변재혁</span>
    <span class="accountnumber">계좌번호: 123456787</span>
    <span class="stockname">{{ stockname }}</span>
    <span class="stockprice">{{ stockprice }}원</span>
    <span class="stockprice-forcalc">800000원</span>
    <span class="quantity">2주</span>
    <span class="ment">지급받을 수 있는 예상 마일리지</span>
    <span class="mileage-calc">1600</span>
    <span class="plus"> + </span>
    <span class="minus"> - </span>

    <div class="modal" v-show="showConfirmModal">
      <div style="text-align:center; font-size: 2rem">
        <span>매수 주문확인</span>
      </div>
      <div style="width: 100%; height: 0.5px; background-color: lightgray"></div>
      <div>
        <table>
          <tbody>
            <tr>
              <td class="title" style="width: 191px!important">종목이름</td>
              <td class="text">{{ stockname }}</td>
            </tr>
            <tr>
              <td class="title">주문수량</td>
              <td class="text">10주</td>
            </tr>
            <tr>
              <td class="title">주문가격</td>
              <td class="text">{{ stockprice }}주</td>
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
      <div class="buttons" style="width: 340px; margin: 0 auto;">
        <div @click="confirmModalToggle" class="confirmdiv" style="display: inline-block; border: 1px solid gray; border-radius: 10px; width: 155px; height: 50px; position: relative">
          <span style="font-size: 1.2rem; position: absolute; left: 55px; top: 10px; font-weight: bold;">취&nbsp;소</span>
        </div>
        <div class="confirmdiv" style="display: inline-block; background-color: #E02D21; border-radius: 10px; width: 155px; height: 50px; float: right; position: relative;">
          <span style="font-size: 1.2rem; position: absolute; left: 55px; top: 10px; color: white; font-weight: bold;">매&nbsp;수</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';
import axios from 'axios';

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
      showConfirmModal: false,
    };
  },
  methods: {
    confirmClick() {

    },
    notOrder() {

    },
    orderSuccess() {

    },
    confirmModalToggle() {
      this.showConfirmModal = !this.showConfirmModal;
    },
    checkCurrentPrice(stockName) {
      const that = this;
      axios.get('http://127.0.0.1:8000/stock?text=' + stockName)
        .then(response => {
          console.log(response);
          that.stockprice = response.data.current_price;
        })
    },
    getUserInfo() {
      axios.get('http://127.0.0.1:8000/member/' + this.$cookies.get('userPk') + '/')
    }
  },
  created() {
    const stockName = this.$store.getters.getStockName;
    console.log('orderstock에서 현재 조회하고자 하는 stockname 가져오기 >> ' + stockName);
    this.stockname = stockName;
    this.checkCurrentPrice(stockName)
  }
}
</script>

<style scoped>
table {
  width: 340px;
}
.confirmdiv:hover {
  cursor: pointer;
}
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
  font-size: 1.5rem;
  top: 280px;
  left: 34px;
}

.accountnumber {
  top: 0px;
  left: 0px;
  font-size: 1.2rem;
  top: 285px;
  left: 170px;
}

.stockname {
  top: 148px;
  left: 55px;
  font-size: 1.5rem;
}

.stockprice {
  top: 210px;
  left: 25px;
  font-size: 2rem;
}

.stockprice-forcalc {
  top: 620px;
  right: 90px;
  font-size: 1.2rem;
}

.quantity {
  top: 572px;
  right: 123px;
  font-size: 1.2rem;
}

.mileage-calc {
  top: 500px;
  right: 235px;
  font-size: 1.5rem;
}

.ment {
  top: 470px;
  right: 18px;
  font-size: 1.3rem;
}

.text {
  text-align: right;
}

.modal {
  background: #fff;
  border-radius: 2px;
  display: inline-block;
  height: 375px;
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
  font-size: 1.4rem;
}
td {
  height: 50px;
}

.text {
  font-size: 1.2rem;
}

table {
  margin-left: 31px;
}
</style>
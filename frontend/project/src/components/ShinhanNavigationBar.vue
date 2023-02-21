<template>
  <nav>
    <ol class="shinhan-header" ref="header">
      <li class="shinhan-header-link">
        <a href="#"
          >뉴스<br />커뮤니티</a
        >
      </li>
      <li class="shinhan-header-link">
        <a href="#" 
          >친환경<br />마일리지</a
        >
      </li>
      <li class="shinhan-header-link">
        <a href="#"
          >친환경<br />계좌</a
        >
      </li>
      <li class="shinhan-header-link">
        <a href="#" 
          >친환경<br />미션</a
        >
      </li>
      <li class="shinhan-header-link">
        <a href="#" 
          >친환경<br />주식</a
        >
      </li>
      <li class="shinhan-header-link">
        <img
          :src="require('../assets/shinhannavigationbar/bell-new.svg')"
          alt=""
        />
      </li>
    </ol>
  </nav>
</template>

<script>
export default {

};
</script>

<style scoped>
* {
  font-size: 1.2rem!important;
}
.active {
  font-weight: bold!important;
  font-size: 1.2rem!important;
}

.inactive {
  font-weight: lighter!important;
  color: grey!important;
  font-size: 1rem!important;
}
.shinhan-header {
  list-style-type: none;
  overflow: hidden;
  background-color: white;
}

.shinhan-header > li {
  float: left;
  width: 80px;
  height: 75px;
  display: table;
  position: relative;
}

.shinhan-header li a {
  width: 100%;
  height: 100%;
  font-size: 14px;
  color: black;
  text-decoration: none;

  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

.shinhan-header li img {
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.shinhan-header li a:hover {
  font-weight: bold;
}
</style>
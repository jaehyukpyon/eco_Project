<template>
  <footer>
    <ol class="shinhan-footer">
      <li class="shinhan-footer-link">
        <img src="../assets/shinhanfooternavigation/Hamburger_MD.svg" alt="" />
      </li>
      <li class="shinhan-footer-link">
        <a href="#">홈</a>
      </li>
      <li class="shinhan-footer-link active">
        <a href="#">친환경</a>
      </li>
      <li class="shinhan-footer-link">
        <a href="#">관심<br />종목</a>
      </li>
      <li class="shinhan-footer-link">
        <a href="#">현재가</a>
      </li>
      <li class="shinhan-footer-link">
        <a href="#">주식<br />주문</a>
      </li>
    </ol>
  </footer>
</template>

<script>
export default {};
</script>

<style scoped>
* {
  font-size: 1rem!important;
}
.active {
  font-weight: bold;
}
.shinhan-footer {
  list-style-type: none;
  overflow: hidden;
  background-color: white;
}

.shinhan-footer>li {
  float: left;
  width: 80px;
  height: 75px;
  display: table;
  position: relative;
}

.shinhan-footer li a {
  width: 100%;
  height: 100%;
  font-size: 14px;
  color: black;
  text-decoration: none;

  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

.shinhan-footer li img {
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

footer {
  position: absolute;
  bottom: 0px;
}
</style>
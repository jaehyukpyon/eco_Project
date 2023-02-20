<template>
  <div>
    <div style="margin-top: 30px; margin-left: 35px; position: relative">
      <span class="name">이관현</span>
      <img src="../assets/mileage/currentmileage.png" alt="" />
      <span class="total">3000</span>
    </div>

    <div style="margin-top: 25px">
      <table style="text-align: center; margin: 0 auto; width: 100%">
        <thead>
          <tr>
            <th>유형</th>
            <th>적립(+)/사용(-)</th>
            <th>날짜</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
          <tr>
            <td>일일미션</td>
            <td>100</td>
            <td>2023-02-20 11:54</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  beforeCreate() {
    this.$emit("barType", "green");
  },
};
</script>

<style scoped>
.name {
  top: 25px;
  left: 28px;
  position: absolute;
  font-weight: bolder;
  font-size: 20px;
}
.total {
  position: absolute;
  top: 90px;
  right: 95px;
  font-size: 30px;
}
table thead tr th {
  font-size: 22px;
  height: 50px;
}
table tbody tr td {
  font-size: 18px;
  height: 30px;
}
</style>
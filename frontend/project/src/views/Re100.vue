<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="text-align: center;">
      <img src="../assets/re100/re100.png" alt="">
    </div>
    <div style="height: 328px; overflow: auto; background='red';">
      <table style="text-align: center; width: 100%">
        <thead>
          <tr>
            <th>No.</th>
            <th>기업명</th>
            <th>Re100 달성 <br>목표 연도(년)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>27</td>
            <td>삼성바이오로직스</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>26</td>
            <td>삼성전기</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>25</td>
            <td>삼성디스플레이</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>24</td>
            <td>삼성SDI</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>23</td>
            <td>삼성전자</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>22</td>
            <td>네이버</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>21</td>
            <td>LG이노텍</td>
            <td>2030</td>
          </tr>
          <tr>
            <td>20</td>
            <td>KT</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>19</td>
            <td>기아</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>18</td>
            <td>현대자동차</td>
            <td>2045</td>
          </tr>
          <tr>
            <td>17</td>
            <td>현대위아</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>16</td>
            <td>현대모비스</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>15</td>
            <td>인천국제공항공사</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>14</td>
            <td>롯데칠성음료</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>13</td>
            <td>SK아이이테크놀로지</td>
            <td>2030</td>
          </tr>
          <tr>
            <td>12</td>
            <td>미래에셋증권</td>
            <td>2025</td>
          </tr>
          <tr>
            <td>11</td>
            <td>고려아연</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>10</td>
            <td>KB금융그룹</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>9</td>
            <td>한국수자원공사</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>8</td>
            <td>LG에너지솔루션</td>
            <td>2030</td>
          </tr>
          <tr>
            <td>7</td>
            <td>아모레퍼시픽</td>
            <td>2030</td>
          </tr>
          <tr>
            <td>6</td>
            <td>SKC</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>5</td>
            <td>SK실트론</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>4</td>
            <td>SK머티리얼즈</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>3</td>
            <td>㈜SK</td>
            <td>2040</td>
          </tr>
          <tr>
            <td>2</td>
            <td>SK텔레콤</td>
            <td>2050</td>
          </tr>
          <tr>
            <td>1</td>
            <td>SK하이닉스</td>
            <td>2050</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';
export default {
  components: {
    ShinhanNavigationBar,
  },
}
</script>

<style scoped>
table thead th {
  height: 45px;
  font-size: 1.3rem;
}

th, td {
  width: 33.333%;
}
tbody td {
  height: 40px;
  font-size: 1.2rem;
}
</style>
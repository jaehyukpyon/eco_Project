<template>
    <div class="container">
      <h1>회원가입</h1>
  
      <div style="text-align: center;">
        <img src="../assets/shinhancharacter/character2.png" alt="">
      </div>
  
      <label for="uname"><b>유저네임</b></label>
      <input type="text" placeholder="사용하실 유저네임을 입력하세요." name="username" id="username" required />
  
      <label for="psw"><b>비밀번호</b></label>
      <input type="password" placeholder="사용하실 비밀번호를 입력하세요." name="password" id="password" required />
  
      <button type="submit">회원가입하기</button>
    </div>
  </template>
  
  <script>
  export default {};
  </script>
  
  <style scope>
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }
  
  /* Set a style for all buttons */
  button {
    background-color: #A3C7F7;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    font-size: 1.2rem;
  }
  
  /* Add a hover effect for buttons */
  button:hover {
    opacity: 0.8;
  }
  /* Add padding to containers */
  .container {
    padding: 16px;
  }
  
  /* The "Forgot password" text */
  span.psw {
    float: right;
    padding-top: 16px;
  }
  </style>
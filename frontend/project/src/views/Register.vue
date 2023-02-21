<template>
    <div class="container">
      <h1>회원가입</h1>
  
      <div style="text-align: center;">
        <img src="../assets/shinhancharacter/character2.png" alt="">
      </div>
  
      <label for="uname"><b>유저네임</b></label>
      <input type="text" placeholder="사용하실 유저네임을 입력하세요." name="username" id="username" required ref="username" />
  
      <label for="psw"><b>비밀번호</b></label>
      <input type="password" placeholder="사용하실 비밀번호를 입력하세요." name="password" id="password" required ref="password" />
  
      <button @click="register">회원가입하기</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    methods: {
      register() {
        const username = this.$refs.username.value;
        const password = this.$refs.password.value;

        axios.post('http://127.0.0.1:8000/member/register/', {
          username: username,          
          password: password,
        }).then(response => {
          console.log(response);
          if (response.status == 200) {
            alert('회원가입이 완료되었습니다.');

            axios.get('http://127.0.0.1:8000/member/')
              .then(response => {
                console.log(response);
                response.data.forEach(member => {
                  if (member.username == username) {
                    this.$cookies.set('userId', member.id);
                  }
                });
                console.log('test1'); // 나중에
                this.$router.push('/login');
              });
              console.log('test2'); // 먼저
          } else {
            alert('회원가입 오류 발생.');
          }
        }).catch(error => {
          alert('회원가입 서버 오류 발생.');
        })
      }
    },
  };
  </script>
  
  <style scoped>
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
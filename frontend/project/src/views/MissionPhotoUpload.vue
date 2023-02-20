<template>
  <div>
    <div class="top-wrap">
      <img src="../assets/missionphotoupload/greenrectangle.png" alt="" />
      <div class="mission-text">
        <p>
          <span class="mission-type">텀블러 사용하기</span><br /><br />
          <span class="mission-description"
            >카페에서 텀블러를<br />사용한 사진을<br />업로드 해주세요!</span
          >
        </p>
      </div>
    </div>

    <div style="margin-top: 15px">
      <div style="text-align: center">
        <label for="file-upload" class="custom-file-upload">
          여기를 클릭해서 파일을 업로드 해주세요!
        </label>
      </div>
      <input type="file" @change="onFileChange" id="file-upload" />
      <div id="preview" style="margin-top: 10px">
        <img v-if="url" :src="url" width="480" height="325" />
      </div>
    </div>

    <div v-if="url" style="text-align: center;">
      <img src="../assets/missionphotoupload/uploadbtn.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      url: null,
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
  },
  beforeCreate() {
    this.$emit("sendCurrentPath", this.$route.path);
    this.$emit("barType", "shinhan");
  },
};
</script>

<style scoped>
input[type="file"] {
  display: none;
}
.custom-file-upload {
  border: 1px solid #ccc;
  display: inline-block;
  padding: 6px 12px;
  cursor: pointer;
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
.image-thumbnail {
  margin-top: 20px;
  margin-left: 16px;
  width: 450px;
  height: 360px;
  background-color: antiquewhite;
  border-radius: 20px;
}
.mission-type {
  font-size: 1.5rem;
}

.mission-description {
  font-size: 1.2rem;
}
.top-wrap {
  margin-top: 20px;
  position: relative;
  text-align: center;
}
.top-wrap .mission-text {
  display: flex;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  align-items: center;
  justify-content: center;
}
</style>
<template>
  <div id="researchinfo">
    <p class="researchinfo">
      <b>Aeternity中国研究院成员来自以下院校</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <img :src="img_url.img_url">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResearchInfo',
  data: function () {
    return {
      img_url: ''
    }
  },
  methods: {
    getSchoolInfo: function () {
      this.$axios.get('/api/institute/school_info/', {
        params: {
          page: 'research'
        }
      }).then(response => {
        if (response.data.status === 2000) {
          console.log(response.data.result.datas)
          this._data.img_url = response.data.result.datas[0]
        } else {
          console.log(response.data.message)
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.getSchoolInfo()
  }
}
</script>

<style scoped>
  #researchinfo {
    padding: 0 7%;
    padding-top: 160px;
    padding-bottom: 100px;
  }
  #researchinfo>.body {
    padding: 40px 0;
  }
  #researchinfo>.body>img {
    border: 1px dashed #333333;
    width: 100%;
  }
  #researchinfo>.researchinfo{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #researchinfo>.researchinfo p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #researchinfo>.researchinfo>b {
    color: #292929;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
</style>

<template>
  <div id="introduction">
    <el-row>
      <el-col :span="10" class="introduction">
        <p class="info">
          <b>AeternityChina研究院</b><br>
          <span>Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life</span>
        </p>
        <button id="connect_me">联系我们 >> </button>
      </el-col>
      <el-col :span="14">
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Introduction'
}
</script>

<style scoped>
  #introduction{
    margin-top: 52px;
    border-bottom: 1px solid #f5f5f5;
    width: 100%;
    height: 900px;
    background: #F0F0F0 url("/static/images/foundation_bg.png") no-repeat center 160px;
    text-align: left;
  }
  #introduction .introduction {
    padding: 270px 0;
  }
  #introduction .introduction .info{
    width: 445px;
    margin-left: 200px;
    text-align: left;
  }
  #introduction .introduction .info>b{
    font-size: 1.8em;
    letter-spacing: 3px;
  }
  #introduction .introduction .info>span{
    font-size: 1em;
    color: #888888;
    position: relative;
    top: 7px;
  }
  #connect_me{
    margin-top: 70px;
    width: 320px;
    color: #ffffff;
    margin-left: 200px;
    background: #333333;
    padding-top: 10px;
    padding-bottom: 10px;
    border: 1px solid #333333;
    cursor: pointer;
  }
</style>

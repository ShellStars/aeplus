<template>
  <div id="taginfo">
    <p class="taginfo">
      <b>AeternityChina基金</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <el-row>
        <el-col :span="8">
          <div>
            <img src="/static/images/foundation_tag_logo1.png"/>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/foundation_tag_logo2.png"/>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/foundation_tag_logo3.png"/>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TagInfo'
}
</script>

<style scoped>
  #taginfo {
    height: 380px;
    padding: 160px 20% 100px 20%;
    background:url("/static/images/foundation_tag_bg.png") no-repeat center 0;
  }
  #taginfo>.taginfo{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #taginfo>.body{
    padding-top: 120px;
  }
  #taginfo>button{
    margin-left: auto;
    margin-right: auto;
    margin-top: 100px;
    width: 40%;
    background: #292929;
    color: #FFFFFF;
    padding-top: 15px;
    padding-bottom: 15px;
    border: 1px solid #292929;
  }
  #taginfo>.body p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #taginfo>.body img{
    width: 80%;
  }
  #taginfo>.taginfo>b {
    color: #ffffff;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
</style>

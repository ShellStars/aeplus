<template>
  <div id="aefoundation">
    <p class="aefoundation">
      <b>AeternityChina基金</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <el-row>
        <el-col :span="8">
          <div>
            <img src="/static/images/open.png"/>
            <p style="text-align: center; color: #333333; font-size: 1.2em;"><b>生态</b></p>
            <p>With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/share.png"/>
            <p style="text-align: center; color: #333333; font-size: 1.2em;"><b>服务</b></p>
            <p>With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/enterprising.png"/>
            <p style="text-align: center; color: #333333; font-size: 1.2em;"><b>专注</b></p>
            <p>With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
          </div>
        </el-col>
      </el-row>
    </div>
    <button>深入理解 >> </button>
  </div>
</template>

<script>
export default {
  name: 'AeternityFoundation'
}
</script>

<style scoped>
  #aefoundation {
    height: 700px;
    padding: 160px 20% 100px 20%;
    background-color: #F0F0F0;
  }
  #aefoundation>.aefoundation{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #aefoundation>.body{
    margin-top: 120px;
  }
  #aefoundation>button{
    margin-left: auto;
    margin-right: auto;
    margin-top: 100px;
    width: 40%;
    background: #292929;
    color: #FFFFFF;
    padding-top: 15px;
    padding-bottom: 15px;
    border: 1px solid #292929;
    cursor: pointer;
  }
  #aefoundation>.body p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #aefoundation>.aefoundation>b {
    color: #292929;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
</style>

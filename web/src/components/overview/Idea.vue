<template>
  <div id="idea">
    <p class="idea">
      <b>理念</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <el-row>
        <el-col :span="8">
          <div>
            <img src="/static/images/open.png"/>
            <p>With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/share.png"/>
            <p>With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <img src="/static/images/enterprising.png"/>
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
  name: 'Idea'
}
</script>

<style scoped>
  #idea {
    height: 700px;
    padding: 160px 20% 100px 20%;
  }
  #idea>.idea{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #idea>.body{
    margin-top: 120px;
  }
  #idea>button{
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
  #idea>.body p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #idea>.idea>b {
    color: #292929;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
</style>

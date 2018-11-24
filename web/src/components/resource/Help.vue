<template>
  <div id="help">
    <p class="help">
      <b>获得帮助</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING <WHIT></WHIT>
    </p>
    <div class="body">
      <p>With powerful features, an intuitive interface  and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.</p>
      <button>联系我们 >></button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Help'
}
</script>

<style scoped>
  #help {
    height: 380px;
    padding: 160px 10% 100px 10%;
    background:url("/static/images/help_bg.png") no-repeat center 0;
    text-align: left;
  }
  #help>.help{
    color: #f0f0f0;
    margin: 0;
    font-size: 1.0em;
    margin-left: auto;
    margin-right: auto;
  }
  #help>.body{
    padding-top: 60px;
    width: 42%;
  }
  #help>.body>button{
    margin-left: 20%;
    margin-top: 100px;
    width: 40%;
    background: #4E54E2;
    color: #FFFFFF;
    padding-top: 10px;
    padding-bottom: 10px;
    border: 1px solid #4E54E2;
    cursor: pointer;
  }
  #help>.body p{
    text-align: left;
    color: #f0f0f0;
  }
  #help>.help>b {
    color: #ffffff;
    font-size: 1.4em;
    letter-spacing: 2px;
  }
</style>

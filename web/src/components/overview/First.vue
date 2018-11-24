<template>
  <div id="first">
    <img id="first_logo" src="/static/images/logo_big.png" />
    <p class="info">
      <b>让Aeternity成为流行</b><br>
      <span>Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life</span>
    </p>
    <button id="join_me">加入我们 >> </button><br>
    <button id="connect_me">联系我们 >> </button>
  </div>
</template>

<script>
export default {
  name: 'First'
}
</script>

<style scoped>
  #first{
    border-bottom: 1px solid #cccccc;
    width: 100%;
    height: 952px;
    background: #F0F0F0 url("/static/images/first_bg.png") no-repeat center 578px;
    background-size: 120% 420px;
  }
  #first>#first_logo{
    margin-top: 343px;
    width: 260px;
  }
  #first>.info{
    width: 320px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
  }
  #first>.info>b{
    font-size: 1.8em;
    letter-spacing: 3px;
  }
  #first>.info>span{
    font-size: 1em;
    color: #888888;
    position: relative;
    top: 7px;
  }
  #join_me {
    margin-top: 15px;
    width: 320px;
    color: #ffffff;
    background: #333333;
    padding-top: 10px;
    padding-bottom: 10px;
    border: 1px solid #333333;
    cursor: pointer;
  }
  #connect_me{
    margin-top: 15px;
    width: 320px;
    padding-top: 10px;
    padding-bottom: 10px;
    background: #ffffff;
    border: 1px solid #aaaaaa;
    cursor: pointer;
  }
</style>

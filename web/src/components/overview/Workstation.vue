<template>
  <div id="workstation">
    <p class="workstation">
      <b>工作站</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <img src="/static/images/map.png">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Workstation'
}
</script>

<style scoped>
  #workstation {
    text-align: left;
    background: #f5f5f5;
    padding: 0 7%;
    padding-top: 160px;
    padding-bottom: 100px;
  }
  #workstation .body {
    padding: 40px 0;
    width: 100%;
  }
  #workstation .body>img{
    width: 100%;
  }
  #workstation>.workstation{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #workstation>.workstation p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #workstation>.workstation>b {
    color: #292929;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
</style>

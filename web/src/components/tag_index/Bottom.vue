<template>
  <div id="bottom">
    <el-row>
      <el-col :span="5">
        <label class="first">关于我们</label><br><br><br>
        <div>
          <label>企业介绍</label><br><br>
          <label>了解我们</label><br><br>
          <label>联系我们</label><br><br>
          <label>加入我们</label><br><br>
          <label>推广联盟</label>
        </div>
      </el-col>
      <el-col :span="1" style="padding: 2% 0;">
        <div style="border-left: 1px solid #ffffff; height: 280px;"></div>
      </el-col>
      <el-col :span="5">
        <label class="first">帮助中心</label><br><br><br>
        <div>
          <label>支付问题</label><br><br>
          <label>课件指南</label><br><br>
          <label>售后政策</label><br><br>
          <label>应用下载</label>
        </div>
      </el-col>
      <el-col :span="1" style="padding: 2% 0;">
        <div style="border-left: 1px solid #ffffff; height: 280px;"></div>
      </el-col>
      <el-col :span="5">
        <label class="first">关注我们</label><br><br><br>
        <div class="connect_info">
          <label><img src="/static/images/github.png"/> GitHub</label><br><br>
          <label><img src="/static/images/wechart.png"/> 微信</label><br><br>
          <label><img src="/static/images/blog.png"/> 博客</label><br><br>
          <label><img src="/static/images/telegram.png"/> Telegram</label><br><br>
          <label><img src="/static/images/twitter.png"/> Twitter</label>
        </div>
      </el-col>
      <el-col :span="1" style="padding: 2% 0;">
        <div style="border-left: 1px solid #ffffff; height: 280px;"></div>
      </el-col>
      <el-col :span="6">
        <div style="color: #ffffff; text-align: left; padding: 0 20%; margin-top: 5px">
          <img src="/static/images/logo_write.png" />
          <p>
            Aeternity Plus<br>
            <br>
            965291809@qq.com
          </p>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Bottom'
}
</script>

<style scoped>
  #bottom{
    min-width: 700px;
    min-height: 300px;
    background: #292929;
    padding: 63px 15%;
  }
  #bottom .connect_info{
    text-align: left;
    width: 100px;
    margin: auto;
  }
  #bottom label{
    color: #ffffff;
    font-size: 1em;
    cursor: pointer;
    width: 5%;
  }
  #bottom label[class=first]{
    font-size: 1.4em;
  }
  #bottom label img{
    vertical-align: -20%;
  }
</style>

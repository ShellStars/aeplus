<template>
  <div class="progressresource">
    <div class="title">
      <p>
        <b>{{card_name}}</b>&nbsp;&nbsp;<span>{{card_introduce}}</span>
      </p>
    </div>
    <div class="body">
      <div class="item_info" v-for="(item, index) in data_list" :key="index">
        <div class="img_info">
          <el-tooltip class="item" effect="light" placement="bottom">
            <div slot="content" style="width: 200px;">{{item.img_desc}}</div>
            <img :src="item.img_url" class="image">
          </el-tooltip>
        </div>
        <div style="padding: 14px 0;">
          <span class="img_name">{{item.name}}</span>
          <div class="bottom clearfix">
            <p class="introduce">{{ item.img_desc | max_size }}</p>
            <a href="#" v-if="item.access_url">访问 >></a>
            <a href="#" v-if="item.download_url">下载 >></a>
            <a href="#" v-if="item.use_url">使用教程 >></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProgressResource',
  data: function () {
    return {
      card_name: '进阶资源',
      card_introduce: 'WHETHER',
      data_list: [
        {
          img_url: '/static/images/open.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: '主网协议',
          access_url: '1',
          download_url: '',
          use_url: ''
        },
        {
          img_url: '/static/images/share.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: '开发组件',
          access_url: '1',
          download_url: '',
          use_url: ''
        },
        {
          img_url: '/static/images/enterprising.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Python-SDK',
          access_url: '1',
          download_url: '',
          use_url: ''
        },
        {
          img_url: '/static/images/enterprising.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Java-SDK',
          access_url: '1',
          download_url: '',
          use_url: ''
        },
        {
          img_url: '/static/images/enterprising.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: '挖矿教程',
          access_url: '1',
          download_url: '',
          use_url: ''
        },
        {
          img_url: '/static/images/enterprising.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Java-SDK',
          access_url: '1',
          download_url: '',
          use_url: ''
        }
      ]
    }
  },
  filters: {
    max_size: function (value) {
      if (!value) return ''
      value = value.toString()
      if (value.length > 140) {
        return value.slice(0, 100) + '...'
      }
      return value
    }
  }
}
</script>

<style scoped>
  .progressresource{
    padding: 120px 10% 0 10%;
    text-align: left;
    background-color: #f0f0f0;
  }
  .progressresource>.title{
    color: #292929;
    font-size: 1.8em;
  }
  .progressresource>.title>p>b{
    margin-bottom: 30px;
  }
  .progressresource>.title>p>span{
    color: #888888;
    font-size: 0.7em;
  }
  .progressresource>.body{
    min-height: 200px;
    padding-bottom: 80px;
  }
  .progressresource>.body>.item_info{
    width: 20%;
    margin-right: 1%;
    display: inline-block;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .progressresource>.body .img_info{
    text-align: left;
  }
  .progressresource>.body>.item_info a{
    font-size: 0.6em;
    margin-right: 10px;
    text-decoration:none;
  }
  .progressresource>.body .img_info>img{
    cursor: pointer;
  }
  .progressresource>.body .img_name{
    font-size: 1.1em;
    font-weight: 500;
    color: #000;
  }
  .progressresource>.body .introduce{
    font-size: 0.8em;
    color: #333333;
    height: 50px;
  }

</style>

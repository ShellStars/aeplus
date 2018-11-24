<template>
  <div class="officialdynamics">
    <div class="title">
      <p>
        <b>{{card_name}}</b>&nbsp;&nbsp;<span>{{card_introduce}}</span>
      </p>
    </div>
    <div class="body">
      <div class="item_info" v-for="(item, index) in data_list" :key="index">
        <div class="img_info">
          <img :src="item.img_url" class="image">
        </div>
        <div style="padding: 14px 0; text-align: center;">
          <span class="img_name">{{item.name}}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OfficialDynamics',
  data: function () {
    return {
      card_name: '官方动态',
      card_introduce: 'WHETHER',
      data_list: [
        {
          img_url: '/static/images/facebook_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Facebook'
        },
        {
          img_url: '/static/images/twitter_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/blog_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Facebook'
        },
        {
          img_url: '/static/images/telegram_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/twitter_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/blog_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/twitter_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/telegram_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/blog_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/telegram_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/twitter_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        },
        {
          img_url: '/static/images/blog_big.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing ',
          name: 'Twitter'
        }
      ]
    }
  }
}
</script>

<style scoped>
  .officialdynamics{
    padding: 120px 10% 0 10%;
    text-align: left;
    background-color: #ffffff;
  }
  .officialdynamics>.title{
    color: #292929;
    font-size: 1.8em;
  }
  .officialdynamics>.title>p>b{
    margin-bottom: 30px;
  }
  .officialdynamics>.title>p>span{
    color: #888888;
    font-size: 0.7em;
  }
  .officialdynamics>.body{
    min-height: 200px;
    padding-bottom: 80px;
  }
  .officialdynamics>.body>.item_info{
    width: 7%;
    margin-right: 1%;
    display: inline-block;
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .officialdynamics>.body .img_info{
    text-align: center;
  }
  .officialdynamics>.body .img_info>img{
  }
  .officialdynamics>.body .img_name{
    font-size: 0.9em;
    color: #888888;
  }

</style>

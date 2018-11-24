<template>
    <div class="researchlist">
      <div class="title">
        <p>
          <b>{{card_name}}</b>&nbsp;&nbsp;<span>{{card_introduce}}</span>
        </p>
      </div>
      <div class="body">
        <el-row v-if="data_list.length > 0">
          <el-col :span="6" v-for="(item, index) in data_list.slice(0,4)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.img_desc}}</div>
                  <img :src="item.img_url" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.img_desc | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row v-if="data_list.length > 4">
          <el-col :span="6" v-for="(item, index) in data_list.slice(4,8)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.img_desc}}</div>
                  <img :src="item.img_url" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.img_desc | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row v-if="data_list.length > 8">
          <el-col :span="6" v-for="(item, index) in data_list.slice(8,12)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.img_desc}}</div>
                  <img :src="item.img_url" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.img_desc | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
</template>

<script>
export default {
  name: 'STP',
  data: function () {
    return {
      card_name: '市场营销顾问',
      card_introduce: 'WHETHER',
      data_list: [
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life',
          name: 'Juns'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Whether you’re building a design system or ' +
          'working with.',
          name: '2018-11-13'
        },
        {
          img_url: '/static/images/demo.png',
          img_desc: 'Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life Ntroducing Dark Mode in Sketch. Hit the lights, lose the distractions and watch your designs come to life',
          name: 'Juns'
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
  .researchlist{
    padding: 120px 10% 0 10%;
    text-align: left;
    background-color: #f5f5f5;
  }
  .researchlist>.title{
    color: #292929;
    font-size: 1.8em;
  }
  .researchlist>.title>p>b{
    margin-bottom: 30px;
  }
  .researchlist>.title>p>span{
    color: #888888;
    font-size: 0.7em;
  }
  .researchlist>.body{
    min-height: 200px;
  }
  .researchlist>.body .img_info{
    text-align: center;
  }
  .researchlist>.body .img_info>img{
    width: 217px;
    height: 217px;
    border-radius: 100px;
    cursor: pointer;
  }
  .researchlist>.body .img_name{
    font-size: 1.1em;
    font-weight: 500;
    color: #000;
  }
  .researchlist>.body .introduce{
    font-size: 0.8em;
    color: #333333;
    height: 50px;
  }
</style>

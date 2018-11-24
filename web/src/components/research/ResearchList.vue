<template>
  <div>
    <div class="researchlist" v-for="(research_item, index) in researches_list" :key="research_item + index">
      <div class="title">
        <p>
          <b>{{research_item.name}}</b>&nbsp;&nbsp;<span>{{research_item.introduce}}</span>
        </p>
      </div>
      <div class="body">
        <el-row v-if="research_item.data_list.length > 0">
          <el-col :span="6" v-for="(item, index) in research_item.data_list.slice(0,4)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.summary}}</div>
                  <img :src="item.headpic" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.summary | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row v-if="research_item.data_list.length > 4">
          <el-col :span="6" v-for="(item, index) in research_item.data_list.slice(4,8)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.summary}}</div>
                  <img :src="item.headpic" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.summary | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row v-if="research_item.data_list.length > 8">
          <el-col :span="6" v-for="(item, index) in research_item.data_list.slice(8,12)" :key="item + index" style="padding: 10px;">
            <el-card :body-style="{ padding: '20px 10px' }">
              <div class="img_info">
                <el-tooltip class="item" effect="light" placement="bottom">
                  <div slot="content" style="width: 200px;">{{item.summary}}</div>
                  <img :src="item.headpic" class="image">
                </el-tooltip>
              </div>
              <div style="padding: 14px;">
                <span class="img_name">{{item.name}}</span>
                <div class="bottom clearfix">
                  <p class="introduce">{{ item.summary | max_size }}</p>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResearchList',
  data: function () {
    return {
      researches_list: []
    }
  },
  methods: {
    getRelationList: function (info) {
      let self = this
      this.$axios.get('/api/institute/get_relation_list/', {
        params: {
          page_no: 1,
          page_item: 10,
          page: 'research',
          id: info.id
        }
      }).then(response => {
        if (response.data.status === 2000) {
          console.log(self.researches_list)
          // this._data.middle_info[info.id] = response.data.result.datas
          if (response.data.result.datas.length > 0) {
            info.data_list = response.data.result.datas
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    getTagList: function () {
      let self = this
      self.$axios.get('/api/institute/get_tag_list/', {
        params: {
          page: 'research'
        }
      }).then(response => {
        if (response.data.status === 2000) {
          // response.data.result.datas.forEach(function (item) {
          //   item.date_list = []
          //   if (item.introduce === undefined) {
          //     item.introduce = 'WHETHER'
          //   }
          //   // self.$options.methods.getRelationList.bind(self)(item)
          // })
          response.data.result.datas.forEach(function (item) {
            item.data_list = []
            if (item.introduce === undefined) {
              item.introduce = 'WHETHER'
            }
            self.$options.methods.getRelationList.bind(self)(item)
          })
          self.researches_list = response.data.result.datas
          console.log(self.researches_list)
        } else {
          console.log(response.data.message)
        }
      }).catch(err => {
        console.log(err)
      })
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
  },
  mounted: function () {
    this.getTagList()
  }
}
</script>

<style scoped>
  .researchlist{
    padding: 60px 10% 60px 10%;
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

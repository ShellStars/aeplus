<template>
  <div id="cooperate">
    <p class="cooperate">
      <b>合作伙伴</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <div v-if="cooperate_list.length > 0">
        <el-row>
          <el-col :span="6" v-for="(cooperate_item, index) in cooperate_list.slice(0,4)" :key="cooperate_item + index">
            <div class="cooperate_item">
              <div class="img" @click="toUrl(cooperate_item)">
                <img :src="cooperate_item.logopic"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div><div v-if="cooperate_list.length > 0">
        <el-row>
          <el-col :span="6" v-for="(cooperate_item, index) in cooperate_list.slice(4,8)" :key="cooperate_item + index">
            <div class="cooperate_item">
              <div class="img" @click="toUrl(cooperate_item)">
                <img :src="cooperate_item.logopic"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
      <div v-if="cooperate_list.length > 4">
        <el-row>
          <el-col :span="6" v-for="(cooperate_item, index) in cooperate_list.slice(8,12)" :key="cooperate_item + index">
            <div class="cooperate_item">
              <div class="img" @click="toUrl(cooperate_item)">
                <img :src="cooperate_item.logopic"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
      <div v-if="cooperate_list.length > 8">
        <el-row>
          <el-col :span="6" v-for="(cooperate_item, index) in cooperate_list.slice(12,16)" :key="cooperate_item + index">
            <div class="cooperate_item" >
              <div class="img" @click="toUrl(cooperate_item)">
                <img :src="cooperate_item.logopic"/>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cooperate',
  data: function () {
    return {
      cooperate_list: []
    }
  },
  methods: {
    toUrl: function (item) {
      window.open(item.link)
    },
    getPartnerList: function () {
      this.$axios.get('/api/api/partner/get_partner_list/', {
        params: {
          page_no: 1,
          page_item: 10,
          page: 'overview'
        }
      }).then(response => {
        if (response.data.status === 2000) {
          this._data.cooperate_list = response.data.result.datas
        } else {
          console.log(response.data.message)
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.getPartnerList()
  }
}
</script>

<style scoped>
  #cooperate {
    background: #f5f5f5;
    padding: 180px 20% 140px 20%;
  }
  #cooperate>.cooperate{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #cooperate>.cooperate b{
    color: #292929;
    font-size: 1.8em;
  }
  #cooperate>.body{
    margin-top: 80px;
  }
  #cooperate>.body>div{
    margin-top: 15px;
  }
  #cooperate>.body .img{
    height:100px;
    cursor: pointer;
  }
  #cooperate>.body .img>img{
    width: 100%;
    height: 100px;
  }
  #cooperate>.body .cooperate_item{
    margin: 0 20%;
  }
</style>

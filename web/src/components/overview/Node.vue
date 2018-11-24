<template>
  <div id="node">
    <p class="node">
      <b>节点</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </p>
    <div class="body">
      <div v-if="node_list.length > 0">
        <el-row>
          <el-col :span="8" v-for="(node_item, index) in node_list.slice(0,3)" :key="node_item + index">
            <div class="node_item">
              <div class="img">
                <img :src="node_item.headpic"/>
              </div>
              <p class="node_des">{{node_item.node_title}}</p>
              <p class="node_time">{{node_item.node_time}}</p>
            </div>
          </el-col>
        </el-row>
      </div>
      <div v-if="node_list.length > 3">
        <el-row>
          <el-col :span="8" v-for="(node_item, index) in node_list.slice(3,6)" :key="node_item + index">
            <div class="node_item">
              <div class="img">
                <img :src="node_item.headpic"/>
              </div>
              <p class="node_des">{{node_item.node_title}}</p>
              <p class="node_time">{{node_item.node_time}}</p>
            </div>
          </el-col>
        </el-row>
      </div>
      <div v-if="node_list.length > 6">
        <el-row>
          <el-col :span="8" v-for="(node_item, index) in node_list.slice(6,9)" :key="node_item + index">
            <div class="node_item">
              <div class="img">
                <img :src="node_item.headpic"/>
              </div>
              <p class="node_des">{{node_item.node_title}}</p>
              <p class="node_time">{{node_item.node_time}}</p>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
    <button>全部节点 >> </button>
  </div>
</template>

<script>
export default {
  name: 'Node',
  data: function () {
    return {
      node_list: []
    }
  },
  methods: {
    getBlogList: function () {
      this.$axios.get('/api/blog/get_blog_list/', {
        params: {
          page_no: 1,
          page_item: 10,
          page: 'overview'
        }
      }).then(response => {
        if (response.data.status === 2000) {
          this._data.node_list = response.data.result.datas
        } else {
          console.log(response.data.message)
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted: function () {
    this.getBlogList()
  }
}
</script>

<style scoped>
  #node{
    background: #f5f5f5;
    padding: 60px 20%;
  }
  #node>.node{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #node>.body{
    margin-top: 50px;
    min-height: 300px;
  }
  #node>button{
    margin-left: auto;
    margin-right: auto;
    margin-top: 60px;
    width: 40%;
    background: #292929;
    color: #FFFFFF;
    padding-top: 15px;
    padding-bottom: 15px;
    border: 1px solid #292929;
    cursor: pointer;
  }
  #node>.node b{
    color: #292929;
    font-size: 1.8em;
  }
  #node>.body>div{
    margin-top: 15px;
  }
  #node>.body .node_item{
    border: 1px solid #cccccc;
    margin: 0 4%;
  }
  #node>.body .img{
    border-bottom: 1px solid #cccccc;
    height: 200px;
  }
  #node>.body .img>img{
    width: 100%;
    height: 200px;
  }
  #node>.body .node_des{
    padding: 8px 10px;
    text-align: left;
    margin: 0;
    color: #292929;
    background-color: #ffffff;
    font-size: 0.9em;
    height: 48px;
    word-wrap: break-word;
  }
  #node>.body .node_time{
    padding: 8px 10px;
    margin: 0;
    text-align: left;
    color: #888888;
    background-color: #ffffff;
    height: 16px;
    font-size: 0.9em;
  }
</style>

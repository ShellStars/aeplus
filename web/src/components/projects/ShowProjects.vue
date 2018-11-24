<template>
  <div id="show_projects">
    <div id="projects_tag">
      <p>
        <b>项目展示</b><br><br>
        WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
      </p>
      <div class="tag_list">
        <p>项目标签</p>
        <div class="tags">
          <div class="tag_item" v-for="(tag, index) in tag_list" @click="ChangeActive(tag)" :class="{active: tag.is_active}" :key="index">
            {{tag.name}} <i v-if="tag.is_active" class="el-icon-check active_icm"></i>
          </div>
        </div>
      </div>
    </div>
    <div id="projects_list">
      <div class="project_item" v-for="(project_item, index) in project_list" :key="index">
        <el-tooltip class="item" effect="light" placement="bottom">
          <div slot="content" style="width: 200px;">{{project_item.summary}}</div>
          <img :src="project_item.logopic" />
        </el-tooltip>
        <p>
          <b>{{project_item.name}}</b><br><br>
          {{project_item.summary|max_size}}<br><br>
          <a :href="project_item.website" target="_blank">官网 >> </a>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShowProjects',
  data: function () {
    return {
      project_list: [],
      tag_list: []
    }
  },
  methods: {
    ChangeActive: function (ActiveTag) {
      console.log(this._data.tag_list)
      let self = this
      self._data.tag_list.forEach(function (item) {
        item.is_active = false
      })
      ActiveTag.is_active = true
      self.$options.methods.getProjectList.bind(self)(ActiveTag)
    },
    getTagList: function () {
      let self = this
      this.$axios.get('/api/api/prolib/get_tag_list/', {
        params: {
          page_no: 1,
          page_item: 10,
          page: 'projects'
        }
      }).then(response => {
        if (response.data.status === 2000) {
          let idx = 1
          response.data.result.datas.forEach(function (item) {
            if (idx === 1) {
              item.is_active = true
              self.$options.methods.getProjectList.bind(self)(item)
              idx += 1
            } else {
              item.is_active = false
            }
          })
          self.tag_list = response.data.result.datas
        } else {
          console.log(response.data.message)
        }
      }).catch(err => {
        console.log(err)
      })
    },
    getProjectList: function (info) {
      let self = this
      this.$axios.get('/api/api/prolib/get_projects_list/', {
        params: {
          page_no: 1,
          page_item: 10,
          page: 'projects',
          id: info.id
        }
      }).then(response => {
        if (response.data.status === 2000) {
          self.project_list = response.data.result.datas
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
      if (value.length > 80) {
        return value.slice(0, 60) + '...'
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
  #show_projects{
    padding-left: 20%;
    padding-right: 5%;
    text-align: left;
    margin-bottom: 20px;
  }
  #projects_tag>p{
    font-size: 0.9em;
    color: #888888;
  }
  #projects_tag>p>b{
    font-size: 1.2em;
    color: #333333;
  }
  #projects_tag>.tag_list{
    margin-top: 30px;
  }
  #projects_tag>.tag_list>p{
    font-size: 0.9em;
    color: #888888;
  }
  #projects_tag>.tag_list>.tags{
    margin-bottom: 80px;
  }
  #projects_tag>.tag_list .tag_item{
    width: 10%;
    height: 26px;
    line-height: 26px;
    margin-right: 2%;
    display: inline-block;
    text-align: center;
    cursor: pointer;
    border: 1px solid #333333;
    color: #333333;
    margin-bottom: 10px;
    background-color: #ffffff;
    border-radius: 0;
  }
  #projects_tag>.tag_list .tag_item>.active_icm{
    color: #ffffff;
    float: right;
    position: relative;
    width: 0;
    height: 0;
    border-width: 13px;
    border-style: solid;
    border-color: transparent #4E54E2 #4E54E2 transparent;
  }
  #projects_tag>.tag_list .active{
    border: 2px solid #4E54E2;
    color: #4E54E2;
  }
  #projects_list>.project_item {
    width: 20%;
    margin-right: 1%;
    display: inline-block;
    border: 1px solid#f0f0f0;
    margin-bottom: 15px;
  }
  #projects_list>.project_item img{
    width: 100%;
  }
  #projects_list>.project_item p{
    padding: 0 10px 10px 10px;
    font-size: 0.8em;
    color: #888888;
  }
  #projects_list>.project_item p>b{
    font-size: 1.2em;
    color: #333333;
  }
  #projects_list>.project_item p>a{
    text-decoration : none;
    color: #666666;
  }
</style>

<template>
  <div id="tag_indexes" v-if="has_url">
    <label id="logo">
      <img src="/static/images/logo.png"/>
    </label>
    <div id="language">
    <el-select v-model="value" placeholder="请选择">
      <el-option
        v-for="item in language"
        :key="item.name"
        :label="item.label"
        :value="item.name">
      </el-option>
    </el-select>
  </div>
    <div id="url_idx">
      <div v-for="tag_index in tag_indexes" :key="tag_index.name" :class="{active: tag_index.isActive}">
        <a :href="tag_index.url" class="tag_index">{{tag_index.tag}}</a>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name: 'TagIndex',
  data: function () {
    const TagIndexes = [
      {
        name: 'overview',
        tag: '概览',
        url: '#/overview/',
        isActive: true
      },
      {
        name: 'research',
        tag: '研究院',
        url: '#/research/',
        isActive: false
      },
      {
        name: 'foundation',
        tag: '基金',
        url: '#/foundation/',
        isActive: false
      },
      {
        name: 'projects',
        tag: '项目库',
        url: '#/projects/',
        isActive: false
      },
      {
        name: 'resource',
        tag: '资源',
        url: '#/resource/',
        isActive: false
      },
      {
        name: 'ask',
        tag: '咨询',
        url: '#/ask/',
        isActive: false
      }
    ]
    const Language = [{
      name: 'chinese',
      label: '中文'
    }, {
      name: 'english',
      label: 'English'
    }]
    let HasUrl = false
    const url = window.location.hash
    TagIndexes.forEach(function (item) {
      if (item.url.split('/')[1] === url.split('/')[1]) {
        HasUrl = true
        item.isActive = true
      } else {
        item.isActive = false
      }
    })
    return {
      tag_indexes: TagIndexes,
      language: Language,
      has_url: HasUrl,
      value: Language[0].label
    }
  },
  watch: {
    '$route': 'setActive'
  },
  // created: function () {
  //   this.setActive()
  // },
  methods: {
    setActive: function () {
      let HasUrl = false
      this._data.tag_indexes.forEach(function (item) {
        const url = window.location.hash
        if (item.url.split('/')[1] === url.split('/')[1]) {
          HasUrl = true
          item.isActive = true
        } else {
          item.isActive = false
        }
      })
      this._data.has_url = HasUrl
    }
  }
}
</script>

<style scoped>
  #tag_indexes {
    height: 50px;
    width: 100%;
    border: 1px solid #eeeeee;
    position: fixed;
    top: 0;
    background: #fff;
    z-index: 99;
    min-width: 700px;
  }
  #tag_indexes>#url_idx{
    display: inline-block;
    min-width: 30px;
    height: 50px;
    float: right;
    margin-right: 3%;
  }
  #tag_indexes>#language{
    display: inline-block;
    min-width: 70px;
    width: 8%;
    max-width: 100px;
    float: right;
    margin-right: 5%;
    margin-top: 10px;
  }
  #tag_indexes>#logo{
    display: inline-block;
    min-width: 70px;
    width: 8%;
    max-width: 100px;
    margin-top: 12px;
    float: left;
    margin-left: 5%;
  }
  #tag_indexes>#logo img{
    height: 23px;
    cursor: pointer;
  }

  #tag_indexes>#url_idx>div {
    height: 50px;
    display: inline-block;
    line-height: 50px;
  }
  #tag_indexes>#url_idx>.active {
    border-bottom: 2px solid #999999;
  }
  #tag_indexes>#url_idx>div>.tag_index{
    min-width: 50px;
    padding: 5px 10px;
    line-height: 50px;
    text-decoration : none;
    color: #666666;
  }
</style>

<template>
  <div id="email">
    <div class="email">
      <b>订阅</b><br><br>
      WHETHER YOU’RE BUILDING A DESIGN SYSTEM OR WORKING WHIT
    </div>
    <div class="body">
      <el-row>
        <el-col :span="8">
          <p>
            With powerful features, an intuitive interface and an expansive plugin ecosystem, Sketch lets you create your bestwork — from your earliest ideas, through to final designs.
          </p>
        </el-col>
        <el-col :span="14" :offset="2" class="send_email">
          <el-input v-model="inp_email" placeholder="输入邮箱…" class="inp_email"></el-input>
          <button class="btn_email" @click="sendEmail()">订阅 </button>
        </el-col>
      </el-row>
      <el-alert
        v-if="email_error"
        title="发送邮件错误"
        type="error"
        :description="email_error"
        show-icon>
      </el-alert>
      <el-alert
        v-if="email_error"
        title="邮件订阅成功"
        type="success"
        :description="email_sucess"
        show-icon>
      </el-alert>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Email',
  data: function () {
    return {
      inp_email: '',
      email_error: '',
      email_sucess: ''
    }
  },
  methods: {
    sendEmail: function () {
      console.log(this)
      const myReg = /^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/
      const inpEmail = this._data.inp_email
      if (inpEmail === '') {
        this._data.email_error = '请输入邮箱'
        return
      } else if (!myReg.test(inpEmail)) {
        this._data.email_error = '邮箱格式有误'
        return
      }
      this.$axios.post('/api/api/subscribe/addsubscribe/', {
        email: inpEmail,
        page: 'overview'
      }).then(response => {
        if (response.status !== 200) {
          this._data.email_error = ''
          this._data.email_sucess = '邮件订阅成功'
          console.log(response.message)
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
  #email {
    padding: 80px 7%;
    text-align: left;
  }
  #email>.email{
    color: #888888;
    margin: 0;
    font-size: 1.1em;
    margin-left: auto;
    margin-right: auto;
  }
  #email .body {
    padding: 40px 0;
  }
  #email>.email p{
    padding: 0 9%;
    text-align: left;
    color: #888888;
  }
  #email>.email>b {
    color: #292929;
    font-size: 1.8em;
    letter-spacing: 2px;
  }
  #email .body .send_email{
    padding: 35px 0;
  }
  #email .body .send_email>.inp_email{
    width: 60%;
    margin-right: 3%;
  }
  #email .body .send_email>.btn_email{
    width: 15%;
    background: #292929;
    color: #FFFFFF;
    padding-top: 10px;
    padding-bottom: 10px;
    border: 1px solid #292929;
    cursor: pointer;
  }
</style>

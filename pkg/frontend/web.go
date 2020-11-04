package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main(){
	router := gin.Default()
	router.LoadHTMLGlob("views/*.html")
	router.Static("/assets", "./assets")

	user := router.Group("/user")
	{
		user.POST("/signup", routes.UserSignUp)
	}

	router.GET("/", func(ctx *gin.Context){
		ctx.HTML(http.StatusOK, "index.html", gin.H{})
	})
	router.Run(":8000")
}

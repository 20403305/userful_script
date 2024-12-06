package main
// 清理字符串中的 HTML 标签，保留 img 标签
import (
	"fmt"
	"regexp"
	"strings"
)

// 使用正则表达式清理HTML，保留img标签，移除其他标签并保留内容
func cleanHTML(input string) string {
	// 正则表达式用于匹配img标签
	imgTagPattern := `<img[^>]*>`

	// 正则表达式：匹配合法的HTML标签
	otherTagPattern := `<([a-zA-Z][a-zA-Z0-9-]*)[^>]*>|</([a-zA-Z][a-zA-Z0-9-]*)[^>]*>`

	// 提取所有 img 标签
	imgTags := extractImgTags(input, imgTagPattern)

	// 用占位符替换 img 标签
	input = replaceImgTagsWithPlaceholder(input, imgTags)

	// 清除所有其他标签
	re := regexp.MustCompile(otherTagPattern)
	input = re.ReplaceAllString(input, "")

	// 恢复 img 标签
	input = restoreImgTags(input, imgTags)

	return input
}

// 提取 img 标签
func extractImgTags(input, pattern string) []string {
	re := regexp.MustCompile(pattern)
	matches := re.FindAllString(input, -1)
	return matches
}

// 用占位符替换 img 标签
func replaceImgTagsWithPlaceholder(input string, imgTags []string) string {
	// 使用占位符替代 img 标签
	for i, tag := range imgTags {
		// 用 unique 的占位符替代每个 img 标签
		placeholder := fmt.Sprintf("{{imgTag}}%d{{/imgTag}}", i)
		input = strings.Replace(input, tag, placeholder, -1)
	}
	return input
}

// 恢复 img 标签
func restoreImgTags(input string, imgTags []string) string {
	// 逐个恢复 img 标签
	for i, tag := range imgTags {
		placeholder := fmt.Sprintf("{{imgTag}}%d{{/imgTag}}", i)
		input = strings.Replace(input, placeholder, tag, 1)
	}
	return input
}

func main() {
	// 输入字符串
	inputHTML := `<div>
		<p>Hello, world!</p>
		<img src="image1.jpg" alt="Image 1">
		<span>This is a <b>test</b> text.</span>
		<img src="image2.jpg" alt="Image 2">
	</div>`

	// 清理 HTML，保留 img 标签
	result := cleanHTML(inputHTML)

	// 输出清理后的 HTML
	fmt.Println(result)
}

# Usage:
# bundle exec ruby image_magick.rb

def create_directory_if_not_exits(dirname)
  return if File.directory?(dirname)

  FileUtils.mkdir_p(dirname)
end

def convert_image(file_name, percentage)
  output_path = "output/image_magick/#{percentage}/#{file_name}"
  command = "convert input/#{file_name} -fill none -fuzz #{percentage}% -draw 'alpha 0,0 floodfill' -flop  -draw 'alpha 0,0 floodfill' -flop #{output_path}"
  system(command)
  puts "✅ Processed #{file_name} -> #{output_path}"
end

create_directory_if_not_exits('output/image_magick')
percentages = [5, 10, 12, 13, 15]
Dir['input/*'].map { |image| image.gsub('input/', '') }.each do |file_name|
  percentages.each do |percentage|
    create_directory_if_not_exits("output/image_magick/#{percentage}")
    convert_image(file_name, percentage)
  end
end

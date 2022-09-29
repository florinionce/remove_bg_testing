require "remove_bg"
require "fileutils"

# Usage:
# source .env
# bundle exec ruby remove_bg_api.rb

api_key = ENV.fetch("REMOVE_BG_API_KEY")

output_directory = File.expand_path("output/remove_bg_api", __dir__)
FileUtils.mkdir_p(output_directory)

# Find all JPGs & PNGs in input directory
input_images = Dir.glob(File.expand_path("input/*.{jpg,png}", __dir__))
puts "Found #{input_images.count} images to process..."

# Process each image and save to the output directory
input_images.each do |input_image|
  output_path = File.join(output_directory, File.basename(input_image))

  RemoveBg
    .from_file(input_image, api_key: api_key, size: "regular")
    .save(output_path, overwrite: true)

  puts "✅ Processed #{input_image} -> #{output_path}"
end

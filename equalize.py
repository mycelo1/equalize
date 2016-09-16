import sublime, sublime_plugin

class EqualizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    arr_ic_pos = []
    max_column = -1;

    for region in self.view.sel():

      sample = self.view.substr(region)
      sample_pos = 0
      index_adjust = 0

      while True:
        sample_br_index = sample.find("\n", sample_pos)

        if (sample_br_index < 0):
          break

        sample_column = self.view.rowcol(region.begin() + sample_br_index)[1] + 1

        if (sample_column > max_column):
          max_column = sample_column

        arr_ic_pos.append((region.begin() + sample_br_index, sample_column))
        sample_pos = sample_br_index + 1

    if (max_column > 0):
      for ic_tuple in arr_ic_pos[:]:
        pad_size = max_column - ic_tuple[1]

        if (pad_size > 0):
          self.view.insert(edit, ic_tuple[0] + index_adjust, self.repeat(' ', pad_size))
          index_adjust += pad_size

  def repeat(self, chars, count):
    return (chars * count)[:count]

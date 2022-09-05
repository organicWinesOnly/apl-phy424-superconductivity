\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{apl-guide}

\DeclareOption*{%
    \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass[12pt]{article}

%% Set the margins
\RequirePackage[margin=1in]{geometry}

\RequirePackage{xcolor}

%% Figure setup and tools
\RequirePackage{subcaption}
\RequirePackage{wrapfig}
% "standard" width of a wrapped figure
\newlength{\figwidth}\setlength{\figwidth}{7.5cm}
% Set default figure placement to htbp
\makeatletter
\def\fps@figure{htbp}
\makeatother

\RequirePackage{fancyhdr}

\RequirePackage{graphicx}
% Restrict image sizes to \linewidth and \textheight
% Inside of wrapfig environments, this will adjust to fit the width
\makeatletter
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
\makeatother
% Scale images if necessary, so that they will not overflow the page
% margins by default, and it is still possible to overwrite the defaults
% using explicit options in \includegraphics[width, height, ...]{}
\setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}

% Math packages
\RequirePackage{amsmath}
\RequirePackage{amssymb}

% Chemistry
\RequirePackage{chemformula}

% For hyperlinks
% TODO we may want to automate some links like sections, cross-references, etc.
\RequirePackage{bookmark}
% \RequirePackage{xurl} % add URL line breaks if available
\hypersetup{
  hidelinks,
  pdfcreator={LaTeX via pandoc}}


%%%% Metadata
\makeatletter
% Creation date and owner are used for the copyright license
\newcommand{\creation}[1]{\gdef\@creation{#1}}
\newcommand{\@creation}{\@latex@warning@no@line{No \noexpand\creation given}}
\newcommand{\owner}[1]{\gdef\@owner{#1}}
\newcommand{\@owner}{University of Toronto}

% The experiment code, used in the header
\newcommand{\experiment}[1]{\gdef\@experiment{#1}}
\newcommand{\@experiment}{\@latex@warning@no@line{No \noexpand\experiment given}}
% Course name
\newcommand{\course}[1]{\gdef\@course{#1}}
\newcommand{\@course}{Advanced Undergraduate Laboratory}
% A picture of the experiment
\newcommand{\labpicture}[1]{\gdef\@labpicture{#1}}

% A history of revisions (must be the contents of a two-column table)
\newcommand{\revisions}[1]{\gdef\@revisions{#1}}
\newcommand{\@revisions}{\@latex@warning@no@line{No \noexpand\revisions given}}
\makeatother

%% License
\makeatletter
\newcommand{\license}{%
    \parbox{.2\textwidth}{\includegraphics[]{copyright-by-nc-sa.pdf}}
    ~~\parbox{.75\textwidth}{%
    \copyright{} \@creation{} \@owner\\%
    This work is licensed under the Creative Commons
    Attribution-NonComercial-ShareAlike 4.0 Unported License\\
    (\url{http://creativecommons.org/licenses/oby-nc-sa/4.0/})}
    }

%% For the lab picture
\newcommand{\@insert@picture}{%
    \@ifundefined{@labpicture}{%
        \@latex@warning@no@line{No \noexpand\labpicture given}%
        \vskip 10cm%
    }{%
        \includegraphics[height=10cm]{\@labpicture}}}
\makeatother

\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}
\let\endchangemargin=\endlist

%% Custom title
\makeatletter
\def\maketitle{\begin{titlepage}%
    \vskip 2em%
    \begin{center}%
        {\large%
        \begin{tabular}{cl}
            \includegraphics[width=.4\textwidth]{Physics-Logo-Black.pdf} &
            \parbox[b]{.55\textwidth}{\MakeUppercase{\@experiment} \\ \@course}
        \end{tabular}}%
        \vskip 2em%
        {\LARGE \@title \par}%
        \vfill %
        \@insert@picture
    \end{center}%
    \begin{changemargin}{.5\textwidth}{0pt}
        {\large
        \lineskip .5em%
        \textbf{Revisions}\par}%
        \hskip 1em%
        \begin{tabular}[t]{rl}%
            \@revisions
        \end{tabular}\par%
    \end{changemargin}
    \par \vfill \noindent\license
    \end{titlepage}%
    \setcounter{footnote}{0}%
    \global\let\title\relax
    \global\let\author\relax
    \global\let\date\relax
    \global\let\owner\relax
    \global\let\experiment\relax
    \global\let\course\relax
    \global\let\revisions\relax
    \global\let\labpicture\relax
    }
\makeatother

\setlength{\emergencystretch}{3em} % prevent overfull lines

%% Headers and footers
\makeatletter
\pagestyle{fancy}
\fancyhf{}
\rhead{\@course}
\lhead{\@experiment}
\cfoot{\thepage}
\makeatother


%% Saftey Reminders environment
\RequirePackage[framemethod=TikZ]{mdframed}

\newcommand{\generalsafety}{%
    \par\vspace{3ex}\par
    \textbf{NOTE}: \emph{This is not a complete list of all hazards; we cannot
    warn against every possible dangerous stupidity, e.g. opening plugged-in
    electrical equipment, juggling cryostats, etc. Experimenters must
    constantly use common sense to assess and avoid risks, e.g. if you spill
    liquid on the floor it will become slippery, sharp edges may cut you,
    etc. If you are unsure whether something is safe, ask the supervising
    professor, the lab technologist, or the lab coordinator. If an accident or
    incident happens, you must let us know. More safety information is available
    at} 
    \url{http://www.ehs.utoronto.ca/resources.htm}.
    }
\newmdenv[%
        outerlinewidth  = 2pt           ,%
        middlelinewidth = 1.5pt           ,%
        innerlinewidth  = 2pt           ,%
        outerlinecolor  = red!70!black  ,%
        middlelinecolor = yellow!40     ,%
        innerlinecolor  = red!70!black  ,%
        %backgroundcolor = yellow!10     ,%
        roundcorner     = 10pt          ,%
        leftmargin      = 20            ,%
        rightmargin     = 20            ,%
        innertopmargin  = \topskip      ,%
        innerbottommargin = \topskip    ,%
        splittopskip    = \topskip      ,%
        frametitle      = {Safety Reminder} ,%
        frametitlefont  = \Large\bfseries   ,%
        frametitlealignment = \centering    ,%
        frametitlerule  = true              ,%
        nobreak,%
    ]{safety}

% vim: filetype=tex
